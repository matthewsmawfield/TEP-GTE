#!/usr/bin/env python3
"""
Generate PDF from built TEP-GTE site using Playwright
"""
import argparse
import os
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

def generate_pdf(quality="maximum", wait_time=5):
    """Generate PDF from the built site"""
    
    # Paths
    base_dir = Path("/Users/matthewsmawfield/www/Temporal Equivalence Principle/TEP-GTE")
    html_path = base_dir / "site" / "dist" / "index.html"
    pdf_name = "5-TEP-GTE-v0.5-Singapore.pdf"
    output_path = base_dir / "site" / "public" / "docs" / pdf_name
    root_output = base_dir / pdf_name
    
    if not html_path.exists():
        print(f"Error: Built site not found at {html_path}")
        print("Run: cd site && node build.js")
        return False
    
    print(f"Generating PDF from: {html_path}")
    print(f"Quality: {quality}, Wait time: {wait_time}s")
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # Load the HTML file
        page.goto(f"file://{html_path}")
        
        # Wait for content to render
        page.wait_for_timeout(wait_time * 1000)
        
        # PDF options based on quality
        pdf_options = {
            "path": str(output_path),
            "format": "A4",
            "margin": {
                "top": "20mm",
                "right": "20mm", 
                "bottom": "20mm",
                "left": "20mm"
            },
            "print_background": True,
            "display_header_footer": False,
        }
        
        if quality == "maximum":
            pdf_options["prefer_css_page_size"] = True
        
        # Generate PDF
        page.pdf(**pdf_options)
        browser.close()
    
    # Copy to root
    import shutil
    shutil.copy2(output_path, root_output)
    
    # Show file sizes
    site_size = output_path.stat().st_size
    root_size = root_output.stat().st_size
    
    print(f"\n✅ PDF generated successfully!")
    print(f"   site/public/docs/{pdf_name}: {site_size:,} bytes ({site_size/1024/1024:.1f} MB)")
    print(f"   {pdf_name}: {root_size:,} bytes ({root_size/1024/1024:.1f} MB)")
    
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate PDF from TEP-GTE site")
    parser.add_argument("--quality", default="maximum", choices=["maximum", "standard"])
    parser.add_argument("--wait-time", type=int, default=5, help="Wait time for rendering (seconds)")
    
    args = parser.parse_args()
    
    success = generate_pdf(quality=args.quality, wait_time=args.wait_time)
    sys.exit(0 if success else 1)
