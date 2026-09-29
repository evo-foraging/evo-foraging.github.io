document.querySelectorAll('[data-figure-source]').forEach(link => {
  const source = window.FIGURE_SOURCES && window.FIGURE_SOURCES[link.dataset.figureSource];
  if (source) { link.href = source; link.textContent = source.toLowerCase().endsWith('.pdf') ? 'Original vector PDF ↗' : 'Original full-resolution PNG ↗'; }
});
