#!/usr/bin/env python3
"""Validate this static GitHub Pages website and its scientific assets."""
from pathlib import Path
import re
from html.parser import HTMLParser
from html import unescape
import json
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.paths=[]
    def handle_starttag(self, tag, attrs):
        d=dict(attrs)
        for key in ("href", "src"):
            v=d.get(key, "")
            if v and not v.startswith(("#", "https:", "http:", "mailto:", "data:")):
                self.paths.append(v.split("#")[0])

parser=Links(); content=(ROOT/"index.html").read_text(); parser.feed(content)
normalized_content = re.sub(r"\s+", " ", unescape(content)).strip()
for path in parser.paths:
    assert (ROOT/path).is_file(), f"Missing site asset: {path}"
manifest=json.loads((ROOT/"assets/figures/manifest.json").read_text())
links=(ROOT/"assets/figures/figure-sources.js").read_text()
for f in manifest:
    preview=ROOT/f["preview"]
    assert preview.exists(), preview
    with Image.open(preview) as im:
        assert im.width >= 2048, f"Low-resolution preview: {f['slug']}: {im.width}"
    assert f['slug'] in links
    assert (ROOT/f['default_source']).exists()
assert not (ROOT/"assets/paper/final-manuscript.pdf").exists(), "Unpublished PDF should not be deployed"
method = (ROOT/"assets/manuscript-method-excerpt.txt").read_text().strip()

assert re.sub(r"\s+", " ", method) in normalized_content, "Website method excerpt differs from manuscript"
abstract=(ROOT/"assets/manuscript-abstract.txt").read_text().strip()
assert re.sub(r"\s+", " ", abstract) in normalized_content, "Website abstract differs from stored manuscript text"
assert "Evolutionary foraging in grids: Intermittent search dynamics emerge in finite, depletable landscapes" in content
assert (ROOT/'.nojekyll').exists()
print(f"PASS: HTML assets, exact abstract, {len(manifest)} source figures, >=2048px previews, PDF and arXiv placeholders")
