# Evolutionary foraging in grids — project website

Minimal static companion website for the accepted NeurIPS 2026 manuscript:

**Evolutionary foraging in grids: Intermittent search dynamics emerge in finite, depletable landscapes**  
Shailendra Bhandari, Alex Szorkovszky, Anis Yazidi, Pedro G. Lind.

**Website:** https://evo-foraging.github.io/  
**Simulation and analysis source code:** https://github.com/shailendrabhandari/intermittent-vs-levy-foraging

## Provenance

The abstract and method excerpt are transcribed from the author-supplied final manuscript (author-supplied accepted manuscript). Figure captions use the corresponding wording from the manuscript; split or cropped panels use only their matching caption sentences. Every original figure supplied by the author is preserved byte-for-byte under `assets/figures/source/`. WebP files under `assets/figures/preview/` are browser previews, not new scientific figures. The two figure PNGs remain downloadable at full resolution.

## Publish with GitHub Pages

1. Use public organization repository `evo-foraging/evo-foraging.github.io`.
2. Put the **contents of this folder** at the repository root, with `index.html` at its top level.
3. In repository Settings → Pages select **Deploy from a branch**, `main`, `/(root)`.
4. The address becomes https://evo-foraging.github.io/ .

If this website repository already exists and contains the previous design, overwrite the corresponding files with these files, review the changes (`git diff`), then commit and push to `main`. You don't need to reinitialize Git or create another repository.

## Update figures

Existing originals: `assets/figures/source/`. Replace a figure by copying a PDF with the same stem; `landscapes.pdf` and `density.pdf` will take precedence over their current PNGs. Then, in a Python environment with the optional rendering dependencies installed:

```bash
python -m pip install -r requirements-render.txt
python scripts/render_figures.py
python scripts/check_site.py
```

Commit **both** your new PDF sources and the regenerated WebP previews plus `assets/figures/figure-sources.js`. The website requires no JavaScript build, hosting services, web fonts, or CDN.

## Verify before publishing

```bash
python scripts/check_site.py
python -m http.server 8000
```

Open http://localhost:8000/ to inspect on your computer.

The original figures and manuscript were supplied by the authors; do not republish modified scientific graphics as originals. The website's CSS and support scripts are under the MIT license in `LICENSE`.

## Paper and arXiv placeholders

The website displays inactive Paper (PDF) and arXiv buttons until public links are available. No manuscript PDF is deployed. Once published, add the actual URLs in both button groups in `index.html` and optionally place a public PDF in `assets/paper/`.
