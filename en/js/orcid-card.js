document.addEventListener('DOMContentLoaded', function() {
  const el = document.getElementById('orcid-card');
  if (!el) return;

  const orcidId = el.dataset.orcid || '0000-0002-9018-6480';
  const jsonPath = `/assets/data/orcid-${orcidId}.json`;

  function renderFallback() {
    el.innerHTML = `<div class="orcid-card">
      <div class="orcid-header">ORCID</div>
      <div class="orcid-body">暂无数据，运行 <code>scripts/fetch_orcid.py ${orcidId}</code> 更新。</div>
    </div>`;
  }

  fetch(jsonPath).then(resp => {
    if (!resp.ok) throw new Error('no json');
    return resp.json();
  }).then(data => {
    // Try to parse common fields from ORCID v3 response
    const person = data.person || {};
    const nameObj = person['name'] || {};
    const given = (nameObj['given-names'] && nameObj['given-names'].value) || '';
    const family = (nameObj['family-name'] && nameObj['family-name'].value) || '';
    const displayName = (given || family) ? `${given} ${family}`.trim() : (data['orcid-identifier'] && data['orcid-identifier'].path) || orcidId;

    const bio = (person['biography'] && person['biography'].content) || '';

    // works summary
    const works = [];
    try {
      const groups = (data['activities-summary'] && data['activities-summary'].works && data['activities-summary'].works.group) || [];
      groups.forEach(g => {
        // each group can have work-summary entries
        const summaries = g['work-summary'] || [];
        summaries.forEach(s => {
          const title = (s['title'] && s['title'].title && s['title'].title.value) || (s['external-ids'] && JSON.stringify(s['external-ids'])) || 'Untitled';
          const putCode = s['put-code'];
          works.push({ title, putCode });
        });
      });
    } catch (e) {
      // ignore
    }

    // Build HTML
    const workHtml = works.slice(0,3).map(w => `<li>${escapeHtml(w.title)}</li>`).join('');
    el.innerHTML = `
      <div class="orcid-card">
        <div class="orcid-left">
          <div class="orcid-avatar">ORCID</div>
        </div>
        <div class="orcid-right">
          <div class="orcid-name">${escapeHtml(displayName)}</div>
          <div class="orcid-id"><a href="https://orcid.org/${orcidId}" target="_blank" rel="noopener">${orcidId}</a></div>
          ${bio ? `<div class="orcid-bio">${escapeHtml(bio)}</div>` : ''}
          ${works.length ? `<div class="orcid-works"><strong>Recent works</strong><ul>${workHtml}</ul></div>` : ''}
        </div>
      </div>
    `;
  }).catch(err => {
    console.warn('Failed to load ORCID JSON:', err);
    renderFallback();
  });

  function escapeHtml(s) {
    if (!s) return '';
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
});
