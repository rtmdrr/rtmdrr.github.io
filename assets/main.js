
async function loadJSON(path) {
  const res = await fetch(path);
  if (!res.ok) throw new Error(`Failed to load ${path}`);
  return await res.json();
}
function html(strings, ...values) { return strings.reduce((acc, s, i) => acc + s + (values[i] ?? ""), ""); }
function renderLinks(links) { return Object.entries(links).map(([k, v]) => html`<a href="${v}" target="_blank" rel="noopener">${k}</a>`).join(" · "); }
async function hydrateProfile() {
  const el = document.querySelector("#profile"); if (!el) return;
  const p = await loadJSON("data/profile.json");
  el.innerHTML = html`
    <div class="hero">
      <div class="container">
        <div class="grid" style="grid-template-columns: 1.2fr .8fr;">
          <div>
            <div class="kicker">${p.affiliation}</div>
            <h1>${p.name}</h1>
            <p class="meta">${p.title} • ${p.location}</p>
            <p>${p.bio}</p>
            <p class="inline">
              <span class="badge">${p.email}</span>
              <span>·</span>
              <span>${renderLinks(p.links)}</span>
            </p>
          </div>
          <div>
          <img src="${p.photo}" alt="${p.name}" style="display:flex; justify-content:center; align-items:center;" />
          </div>
        </div>
      </div>
    </div>
  `;
}
function groupBy(arr, keyFn) { return arr.reduce((acc, x) => { const k = keyFn(x); (acc[k] ||= []).push(x); return acc; }, {}); }
async function hydratePublications() {
  const el = document.querySelector("#pubs"); if (!el) return;
  const pubs = await loadJSON("data/publications.json");
  pubs.sort((a,b) => (b.year||0) - (a.year||0));
  const grouped = groupBy(pubs, p => p.year || "Other");
  const years = Object.keys(grouped).sort((a,b)=> b - a);
  el.innerHTML = years.map(year => html`
    <div class="year">${year}</div>
    <div class="grid" style="grid-template-columns: 1fr;">
      ${grouped[year].map(p => html`
        <article class="pub">
          <h3><a href="${p.url || '#'}" target="_blank" rel="noopener">${p.title}</a></h3>
          <div class="meta">${Array.isArray(p.authors) ? p.authors.join(", ") : p.authors}</div>
          <div class="meta"><span class="tag">${p.venue || ''}</span></div>
        </article>
      `).join("")}
    </div>
  `).join("");
}
async function hydrateTalks() {
  const el = document.querySelector("#talks"); if (!el) return;
  const t = await loadJSON("data/talks.json");
  t.sort((a,b)=> new Date(b.date) - new Date(a.date));
  el.innerHTML = t.map(x => html`
    <article class="card">
      <h3>${x.title}</h3>
      <div class="meta">${new Date(x.date).toLocaleDateString()} • ${x.event}</div>
      ${x.link ? html`<p><a href="${x.link}" target="_blank" rel="noopener">link</a></p>` : ""}
    </article>
  `).join("");
}
async function hydrateTeaching() {
  const el = document.querySelector("#teaching"); if (!el) return;
  const data = await loadJSON("data/teaching.json");
  el.innerHTML = data.map(x => html`
    <article class="card">
      <h3>${x.course}</h3>
      <div class="meta">${x.term}</div>
      ${x.link ? html`<p><a href="${x.link}" target="_blank" rel="noopener">Syllabus / site</a></p>` : ""}
    </article>
  `).join("");
}
async function main() { await hydrateProfile(); await hydratePublications(); await hydrateTalks(); await hydrateTeaching(); }
document.addEventListener("DOMContentLoaded", main);
