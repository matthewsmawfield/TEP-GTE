# TEP-GTE Scripts

PDF generation, compression, and metadata embedding utilities for the
TEP-GTE manuscript (Paper 5, codename Singapore).

All scripts live in `scripts/utils/` and resolve the repository root
relative to their own location (`Path(__file__).resolve().parent.parent.parent`),
so they work from any working directory without hardcoded absolute paths.

## Prerequisites

- Python 3.9+
- [Playwright](https://playwright.dev/) with Chromium installed:
  ```bash
  pip install playwright pypdf pyyaml
  playwright install chromium
  ```
- [Ghostscript](https://www.ghostscript.com/) (`gs`) on the PATH for compression
- [Exiftool](https://exiftool.org/) on the PATH for metadata embedding

## Build the Site First

The PDF pipeline consumes the built site output, so build the static site
before generating the PDF:

```bash
cd "/Users/matthewsmawfield/www/Temporal Equivalence Principle/TEP-GTE/site"
npm run build
```

This assembles the component HTML files in `site/components/*.html` into
`site/dist/index.html` and regenerates the manuscript Markdown.

## Pipeline Overview

The recommended end-to-end pipeline is:

1. **Build the site** (above).
2. **Generate the PDF** from the built site.
3. **Compress the PDF** with Ghostscript.
4. **Embed metadata** from `CITATION.cff` into the PDF.

### 1. `generate_pdf.py` — Generate PDF from HTML

Generates the manuscript PDF from the built site (`site/dist/index.html`)
using Playwright/Chromium. The PDF is written to both
`site/public/docs/5-TEP-GTE-v0.6-Singapore.pdf` and the repository root.

```bash
python scripts/utils/generate_pdf.py --quality maximum --wait-time 5
```

### 2. `html_to_pdf.py` — Advanced HTML to PDF Converter

A general-purpose, configurable HTML-to-PDF converter built on Playwright.
Supports custom page dimensions, scale factors, DPI, margins, headers/footers,
and preset configurations (`high_quality`, `print_ready`, `web_optimized`,
`large_format`).

```bash
python scripts/utils/html_to_pdf.py site/dist/index.html output.pdf --preset high_quality
```

### 3. `compress_pdf.py` — Compress PDF

Compresses a PDF using Ghostscript. Exposes `compress_pdf(input_path,
output_path, quality='ebook')`, which returns a dict with keys
`original_size`, `compressed_size`, and `reduction_percent`. Quality presets:
`screen`, `ebook`, `printer`, `prepress`, `default`.

```bash
python scripts/utils/compress_pdf.py --quality ebook
```

### 4. `embed_pdf_metadata.py` — Embed Metadata

Embeds academic metadata (title, author, subject, keywords) into the
manuscript PDF using `pypdf`. Updates both the root and
`site/public/docs/` copies.

```bash
python scripts/utils/embed_pdf_metadata.py
```

### 5. `process_pdf.py` — Orchestrator

Compresses the PDF and embeds metadata from `CITATION.cff` in one operation.
Reads title, abstract, keywords, version, date, DOI, URL, and authors from the
project's `CITATION.cff`, compresses with Ghostscript, and writes the metadata
using Exiftool.

```bash
python scripts/utils/process_pdf.py <input_pdf> [--quality ebook|printer|prepress|default]
```

Example:

```bash
python scripts/utils/process_pdf.py 5-TEP-GTE-v0.6-Singapore.pdf --quality ebook
```

## Output

- PDF: `5-TEP-GTE-v0.6-Singapore.pdf` (repository root and `site/public/docs/`)
- Site: https://mlsmawfield.com/tep/gte/
- DOI: 10.5281/zenodo.18004832
