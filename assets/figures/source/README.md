# Original figure files

**Original sources are preserved without modification.** Figures from uploaded PDF files retain their vector PDF. Figures supplied as PNG retain their native full resolution.

To replace either PNG with a vector PDF, put your file here using the matching stem:

- `landscapes.pdf` (currently `landscapes.png`)
- `density.pdf` (currently `density.png`)

For any figure PDF update use the same stem as its existing source: `fitness.pdf`, `step-lengths.pdf`, `moments.pdf`, or `movement.pdf`. Then run `python scripts/render_figures.py` from the repository root, commit the updated preview images and `figure-sources.js`. PDF sources are preferred to PNG when both exist. The webpage's original-file link is automatically updated by `figure-sources.js`.
