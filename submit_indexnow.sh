#!/bin/bash
# =============================================================================
# IndexNow Submission Script for TEP-GTE
# =============================================================================
# This script notifies search engines (Bing, Yandex, etc.) when papers are updated.
# Run this after pushing changes to trigger immediate re-crawling.
#
# Usage: ./submit_indexnow.sh
# =============================================================================

# Configuration
HOST="matthewsmawfield.github.io"
KEY="621a69ca2bd75c0778c9658dc1a62f0a"
KEY_LOCATION="https://matthewsmawfield.github.io/TEP-GTE/${KEY}.txt"

# URLs to index (TEP-GTE Synthesis Manuscript)
MAIN_URL="https://matthewsmawfield.github.io/TEP-GTE/"
MAIN_PDF="https://matthewsmawfield.github.io/TEP-GTE/public/Smawfield_2025_TEP-GTE_GlobalTimeEchoes_v0.1_Singapore.pdf"

# JSON Payload
JSON_PAYLOAD=$(cat <<EOF
{
  "host": "$HOST",
  "key": "$KEY",
  "keyLocation": "$KEY_LOCATION",
  "urlList": [
    "$MAIN_URL",
    "$MAIN_PDF"
  ]
}
EOF
)

echo "=============================================="
echo "IndexNow Submission for TEP-GTE"
echo "=============================================="
echo ""
echo "Host: $HOST"
echo "Key Location: $KEY_LOCATION"
echo ""
echo "URLs to index:"
echo "  [TEP-GTE Synthesis Manuscript]"
echo "  - $MAIN_URL"
echo "  - $MAIN_PDF"
echo ""
echo "Submitting to IndexNow API..."
echo ""

# Submit to IndexNow (shared across Bing, Yandex, and other participating engines)
curl -s -X POST "https://api.indexnow.org/indexnow" \
     -H "Content-Type: application/json; charset=utf-8" \
     -d "$JSON_PAYLOAD" \
     -w "\nHTTP Status: %{http_code}\n"

echo ""
echo "=============================================="
echo "Submission complete!"
echo ""
echo "HTTP 200 = Success (URLs received by search engines)"
echo "HTTP 202 = Accepted (URLs queued for processing)"
echo "HTTP 400 = Bad Request (check JSON payload)"
echo "HTTP 403 = Forbidden (key validation failed)"
echo "HTTP 422 = Unprocessable (URLs don't match key location)"
echo "=============================================="
echo ""
echo "Note: Ensure ${KEY}.txt exists at ${KEY_LOCATION}"
