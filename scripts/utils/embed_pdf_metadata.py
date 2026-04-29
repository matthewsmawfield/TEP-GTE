#!/usr/bin/env python3
"""
Embed academic metadata into PDF
"""
from pypdf import PdfReader, PdfWriter
from pathlib import Path

def embed_metadata():
    base_dir = Path("/Users/matthewsmawfield/www/Temporal Equivalence Principle/TEP-GTE")
    pdf_path = base_dir / "5-TEP-GTE-v0.4-Singapore.pdf"
    
    if not pdf_path.exists():
        print(f"Error: PDF not found at {pdf_path}")
        return False
    
    print(f"Embedding metadata into: {pdf_path}")
    
    # Read existing PDF
    reader = PdfReader(str(pdf_path))
    writer = PdfWriter()
    
    # Copy all pages
    for page in reader.pages:
        writer.add_page(page)
    
    # Add metadata
    metadata = {
        "/Title": "Global Time Echoes: Empirical Synthesis",
        "/Author": "Matthew Lukin Smawfield",
        "/Creator": "TEP-GTE Publishing System",
        "/Subject": "Empirical synthesis of the Temporal Equivalence Principle through GNSS clock data analysis",
        "/Keywords": "Temporal Equivalence Principle; GNSS; atomic clocks; CMB alignment; dark matter; gravitational lensing; scalar-tensor gravity; synchronization holonomy; Temporal Topology; Temporal Shear",
    }
    
    writer.add_metadata(metadata)
    
    # Write updated PDF
    with open(pdf_path, "wb") as f:
        writer.write(f)
    
    # Also update the copy in site/public/docs/
    site_pdf = base_dir / "site" / "public" / "docs" / "5-TEP-GTE-v0.4-Singapore.pdf"
    with open(site_pdf, "wb") as f:
        writer.write(f)
    
    print("✅ Metadata embedded successfully!")
    print(f"   Title: {metadata['/Title']}")
    print(f"   Author: {metadata['/Author']}")
    return True

if __name__ == "__main__":
    embed_metadata()
