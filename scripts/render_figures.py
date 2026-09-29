#!/usr/bin/env python3
"""Generate browser-quality previews from original source figures, without altering originals.

Add source/<slug>.pdf to replace an existing PNG, then rerun this script.
A PDF is automatically preferred if both formats exist. Re-run after any replacement.
"""
from pathlib import Path
import json
import fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "assets/figures"
manifest = json.loads((BASE / "manifest.json").read_text())
link_map = {}
for item in manifest:
    slug = item["slug"]
    original = next((BASE / "source" / f"{slug}{ext}" for ext in (".pdf", ".png", ".jpg", ".jpeg") if (BASE / "source" / f"{slug}{ext}").is_file()), None)
    if original is None:
        raise FileNotFoundError(f"Missing original figure: {slug}")
    if original.suffix == ".pdf":
        with fitz.open(original) as doc:
            if len(doc) != 1:
                print(f"Note: {original.name} contains {len(doc)} pages; preview uses page 1")
            page = doc[0]
            scale = 2800 / page.rect.width
            pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), colorspace=fitz.csRGB, alpha=False)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    else:
        img = Image.open(original).convert("RGB")
        # Native pixels retained: no rescaling or destructive preprocessing.
    output = BASE / "preview" / f"{slug}.webp"
    img.save(output, format="WEBP", lossless=True, method=6)
    link_map[slug] = "assets/figures/source/" + original.name
    print(f"{slug:13s}  {img.width} x {img.height}  {original.name}")
(BASE / "figure-sources.js").write_text("window.FIGURE_SOURCES = " + json.dumps(link_map, ensure_ascii=False, indent=2) + ";\n")
print("Previews and source links updated.")
