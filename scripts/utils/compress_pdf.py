#!/usr/bin/env python3
"""
Compress PDF using Ghostscript
"""
import subprocess
from pathlib import Path

# Quality presets mapping to Ghostscript -dPDFSETTINGS
QUALITY_PRESETS = {
    'screen': '/screen',
    'ebook': '/ebook',
    'printer': '/printer',
    'prepress': '/prepress',
    'default': '/default',
}


def compress_pdf(input_path, output_path, quality='ebook'):
    """Compress a PDF using Ghostscript.

    Args:
        input_path: Path to the input PDF file.
        output_path: Path for the compressed output PDF file.
        quality: Compression quality preset (screen, ebook, printer,
            prepress, default). Defaults to 'ebook'.

    Returns:
        dict with keys 'original_size', 'compressed_size',
        'reduction_percent' (all numeric).
    """
    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.exists():
        raise FileNotFoundError(f"PDF not found at {input_path}")

    original_size = input_path.stat().st_size

    pdf_settings = QUALITY_PRESETS.get(quality, '/ebook')

    print(f"Compressing PDF: {input_path}")
    print(f"Original size: {original_size / 1024 / 1024:.1f} MB")
    print(f"Quality: {quality} ({pdf_settings})")

    gs_command = [
        "gs",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        f"-dPDFSETTINGS={pdf_settings}",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        "-dColorImageDownsampleType=/Bicubic",
        "-dColorImageResolution=150",
        "-dGrayImageDownsampleType=/Bicubic",
        "-dGrayImageResolution=150",
        "-dMonoImageDownsampleType=/Bicubic",
        "-dMonoImageResolution=150",
        f"-sOutputFile={output_path}",
        str(input_path)
    ]

    subprocess.run(gs_command, check=True)

    compressed_size = output_path.stat().st_size

    reduction_percent = (1 - compressed_size / original_size) * 100 if original_size else 0.0

    print(f"Compressed size: {compressed_size / 1024 / 1024:.1f} MB")
    print(f"Reduction: {reduction_percent:.1f}%")

    return {
        'original_size': original_size,
        'compressed_size': compressed_size,
        'reduction_percent': reduction_percent,
    }


def _compress_repo_pdfs(quality='ebook'):
    """Compress both the root and site copies of the manuscript PDF.

    Convenience entry point used when running this module directly.
    """
    base_dir = Path(__file__).resolve().parent.parent.parent
    pdf_name = "B5-TEP-GTE-v0.8-Singapore.pdf"
    pdf_path = base_dir / pdf_name
    site_pdf_path = base_dir / "site" / "public" / "docs" / pdf_name

    for path in (pdf_path, site_pdf_path):
        if not path.exists():
            print(f"Warning: PDF not found at {path}, skipping")
            continue
        tmp_path = path.with_suffix(path.suffix + ".tmp")
        compress_pdf(str(path), str(tmp_path), quality=quality)
        subprocess.run(["mv", str(tmp_path), str(path)], check=True)

    return True


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Compress TEP-GTE PDFs")
    parser.add_argument(
        '--quality',
        choices=list(QUALITY_PRESETS.keys()),
        default='ebook',
        help='Compression quality (default: ebook)'
    )
    args = parser.parse_args()
    _compress_repo_pdfs(quality=args.quality)
