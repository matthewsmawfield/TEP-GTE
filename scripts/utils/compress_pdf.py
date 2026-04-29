#!/usr/bin/env python3
"""
Compress PDF using Ghostscript
"""
import subprocess
from pathlib import Path

def compress_pdf():
    base_dir = Path("/Users/matthewsmawfield/www/Temporal Equivalence Principle/TEP-GTE")
    pdf_path = base_dir / "5-TEP-GTE-v0.4-Singapore.pdf"
    site_pdf_path = base_dir / "site" / "public" / "docs" / "5-TEP-GTE-v0.4-Singapore.pdf"
    
    if not pdf_path.exists():
        print(f"Error: PDF not found at {pdf_path}")
        return False
    
    original_size = pdf_path.stat().st_size
    print(f"Compressing PDF: {pdf_path}")
    print(f"Original size: {original_size / 1024 / 1024:.1f} MB")
    
    # Ghostscript compression settings for ebook quality
    gs_command = [
        "gs",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/ebook",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        "-dColorImageDownsampleType=/Bicubic",
        "-dColorImageResolution=150",
        "-dGrayImageDownsampleType=/Bicubic",
        "-dGrayImageResolution=150",
        "-dMonoImageDownsampleType=/Bicubic",
        "-dMonoImageResolution=150",
        f"-sOutputFile={pdf_path}.tmp",
        str(pdf_path)
    ]
    
    # Compress root PDF
    subprocess.run(gs_command, check=True)
    subprocess.run(["mv", f"{pdf_path}.tmp", str(pdf_path)])
    
    # Compress site PDF
    gs_command[-2] = f"-sOutputFile={site_pdf_path}.tmp"
    gs_command[-1] = str(site_pdf_path)
    subprocess.run(gs_command, check=True)
    subprocess.run(["mv", f"{site_pdf_path}.tmp", str(site_pdf_path)])
    
    # Show new sizes
    new_size = pdf_path.stat().st_size
    site_size = site_pdf_path.stat().st_size
    
    print(f"Compressed size (root): {new_size / 1024 / 1024:.1f} MB")
    print(f"Compressed size (site): {site_size / 1024 / 1024:.1f} MB")
    print(f"Reduction: {(1 - new_size / original_size) * 100:.1f}%")
    
    return True

if __name__ == "__main__":
    compress_pdf()
