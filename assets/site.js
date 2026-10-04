// Renders publications from data/publications.json (kept fresh by the GitHub Action).
(function () {
  "use strict";

  var SCHOLAR = "https://scholar.google.com/citations?hl=en&user=ZB0tZNEAAAAJ";
  var ME = /\b(R\.?\s?Dror|Rotem\s+Dror|Dror,\s*R\.?)(?=[\s,.;]|$)/g;

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function itemHTML(p) {
    var title = esc(p.title);
    var href = p.url || p.scholar_url;
    var t = href ? '<a href="' + esc(href) + '">' + title + "</a>" : title;
    var authors = esc(p.authors).replace(ME, '<span class="me">$1</span>');
    var meta = [];
    if (p.citations) meta.push(p.citations + (p.citations === 1 ? " citation" : " citations"));
    if (p.scholar_url && p.url && p.scholar_url !== p.url) meta.push('<a href="' + esc(p.scholar_url) + '">Scholar</a>');
    var venue = esc(p.venue || "");
    if (p.year && venue.indexOf(String(p.year)) === -1) venue += (venue ? ", " : "") + p.year;
    return (
      "<li>" +
      '<span class="pub-title">' + t + "</span>" +
      '<span class="pub-authors">' + authors + "</span>" +
      '<span class="pub-venue">' + venue +
      (meta.length ? '<span class="pub-meta">' + meta.join(" | ") + "</span>" : "") +
      "</span></li>"
    );
  }

  function sortPubs(list) {
    return list.slice().sort(function (a, b) {
      return (b.year || 0) - (a.year || 0);  // stable: keeps Scholar's order within a year
    });
  }

  function renderGrouped(el, pubs) {
    if (!pubs.length) { el.innerHTML = '<p class="empty">No publications match this search.</p>'; return; }
    var html = "", year = null;
    pubs.forEach(function (p) {
      var y = p.year || "Undated";
      if (y !== year) {
        if (year !== null) html += "</ol>";
        html += '<h3 class="pub-year">' + esc(y) + '</h3><ol class="pubs">';
        year = y;
      }
      html += itemHTML(p);
    });
    el.innerHTML = html + "</ol>";
  }

  function fail(el) {
    el.innerHTML = '<p class="empty">The publication list could not be loaded. The full list is on <a href="' + SCHOLAR + '">Google Scholar</a>.</p>';
  }

  function load() {
    return fetch("data/publications.json", { cache: "no-cache" }).then(function (r) {
      if (!r.ok) throw new Error(r.status);
      return r.json();
    });
  }

  // Home page: the most recent few.
  var recent = document.getElementById("recent-pubs");
  if (recent) {
    var n = parseInt(recent.getAttribute("data-limit") || "5", 10);
    load().then(function (d) {
      recent.innerHTML = '<ol class="pubs">' + sortPubs(d.publications).slice(0, n).map(itemHTML).join("") + "</ol>";
    }).catch(function () { fail(recent); });
  }

  // Publications page: full list, grouped by year, with a filter.
  var all = document.getElementById("all-pubs");
  if (all) {
    var box = document.getElementById("pub-filter");
    var count = document.getElementById("pub-count");
    var metrics = document.getElementById("pub-metrics");
    load().then(function (d) {
      var pubs = sortPubs(d.publications);
      var m = d.metrics;
      if (metrics) {
        var bits = [];
        if (m && m.citations) bits.push(m.citations.toLocaleString() + " citations");
        if (m && m.h_index) bits.push("h-index " + m.h_index);
        var txt = bits.length ? bits.join(", ") + ". " : "";
        if (d.updated) txt += "Last updated " + d.updated + ".";
        metrics.textContent = txt;
      }
      function apply() {
        var q = (box && box.value || "").trim().toLowerCase();
        var shown = q ? pubs.filter(function (p) {
          return [p.title, p.authors, p.venue, p.year].join(" ").toLowerCase().indexOf(q) !== -1;
        }) : pubs;
        if (count) count.textContent = shown.length + (shown.length === 1 ? " publication" : " publications");
        renderGrouped(all, shown);
      }
      if (box) box.addEventListener("input", apply);
      apply();
    }).catch(function () { fail(all); });
  }

  // Optional portrait: drop assets/photo.jpg into the repo and it appears.
  var photo = document.querySelector(".profile img");
  if (photo) {
    var hide = function () { photo.remove(); document.querySelector(".profile").classList.remove("has-photo"); };
    if (photo.complete && photo.naturalWidth === 0) hide(); else photo.addEventListener("error", hide);
  }

  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
