document.addEventListener('DOMContentLoaded', function() {
  const el = document.getElementById('scholar-card');
  if (!el) return;

  const user = el.dataset.user || 'Wb4CcQ8AAAAJ';
  const path = `/assets/data/scholar-${user}.json`;

  function renderFallback() {
    el.innerHTML = `<div class="scholar-card">No Scholar snapshot found. Run <code>scripts/fetch_scholar.py ${user}</code> to generate one.</div>`;
  }

  fetch(path).then(r => {
    if (!r.ok) throw new Error('json not found');
    return r.json();
  }).then(data => {
    const name = data.name || '';
    const aff = data.affiliation || '';
    const pubs = (data.publications || []).slice(0,6);

    const pubsHtml = pubs.map(p => {
      const title = escapeHtml(p.title || '');
      const year = escapeHtml(p.year || '');
      const link = p.link ? `<a href="${escapeAttr(p.link)}" target="_blank" rel="noopener">` : '';
      const linkClose = p.link ? '</a>' : '';
      return `<li>${link}${title}${linkClose}${year ? ` <span class="scholar-year">(${year})</span>` : ''}</li>`;
    }).join('');

    const metrics = data.metrics || {};
    let metricsHtml = '';
    if (Object.keys(metrics).length) {
      metricsHtml = '<div class="scholar-metrics"><table>' +
        Object.entries(metrics).map(([k,v]) => `<tr><td>${escapeHtml(k)}</td><td>${escapeHtml(String(v.all||''))}</td></tr>`).join('') +
        '</table></div>';
    }

    el.innerHTML = `
      <div class="scholar-card">
        <div class="scholar-left"><div class="scholar-avatar">GS</div></div>
        <div class="scholar-right">
          <div class="scholar-name">${escapeHtml(name)}</div>
          <div class="scholar-aff">${escapeHtml(aff)}</div>
          ${metricsHtml}
          <div class="scholar-pubs"><strong>Recent publications</strong><ul>${pubsHtml}</ul></div>
          <div class="scholar-link"><a href="https://scholar.google.com/citations?user=${user}" target="_blank" rel="noopener">View full profile on Google Scholar</a></div>
        </div>
      </div>
    `;
  }).catch(err => {
    console.warn('Failed to load scholar JSON', err);
    renderFallback();
  });

  function escapeHtml(s){ if(!s) return ''; return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
  function escapeAttr(s){ return (s||'').replace(/"/g,'&quot;'); }
});
