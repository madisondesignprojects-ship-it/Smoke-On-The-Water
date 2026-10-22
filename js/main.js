(() => {
  const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];

  // Age gate (remembered for 30 days)
  const gate = $('#gate');
  if (gate) {
    const ok = Number(localStorage.getItem('sotw21') || 0) > Date.now();
    if (!ok && !/[?&]nogate/.test(location.search)) {
      gate.hidden = false; document.body.style.overflow = 'hidden';
      $('#gate-yes').focus();
    }
    $('#gate-yes').addEventListener('click', () => {
      localStorage.setItem('sotw21', Date.now() + 30 * 864e5);
      gate.hidden = true; document.body.style.overflow = '';
    });
  }

  // Mobile menu
  const burger = $('#burger'), nav = $('#nav');
  if (burger && nav) {
    const setNav = (open) => { nav.classList.toggle('open', open); burger.setAttribute('aria-expanded', open); burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu'); };
    burger.addEventListener('click', () => setNav(!nav.classList.contains('open')));
    $$('a', nav).forEach(a => a.addEventListener('click', () => setNav(false)));
    document.addEventListener('keydown', e => { if (e.key === 'Escape') setNav(false); });
  }

  // Open-now status + today's hours (all shops: America/Chicago, 10am–9pm daily)
  const parts = new Intl.DateTimeFormat('en-US', { timeZone: 'America/Chicago', weekday: 'short', hour: 'numeric', hour12: false }).formatToParts(new Date());
  const wd = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'].indexOf(parts.find(p => p.type === 'weekday').value);
  const hr = Number(parts.find(p => p.type === 'hour').value) % 24;
  const open = hr >= 10 && hr < 21;
  const s = $('#open-status');
  if (s) {
    s.textContent = open ? 'Open now until 9pm' : (hr < 10 ? 'Closed now · Opens today at 10am' : 'Closed now · Opens tomorrow at 10am');
    if (!open) s.closest('.topbar').classList.add('closed');
  }
  const row = $(`#hours tr[data-d="${wd}"]`); if (row) row.classList.add('today');

  // Lightbox
  const lb = $('#lightbox');
  if (lb) {
    // The viewer image is created on first open, so the page never holds an empty <img>.
    let lbImg = null;
    $$('.g').forEach(b => b.addEventListener('click', () => {
      const i = $('img', b);
      if (!lbImg) { lbImg = document.createElement('img'); lb.appendChild(lbImg); }
      lbImg.src = b.dataset.full; lbImg.alt = i.alt; lb.showModal();
    }));
    lb.addEventListener('click', e => { if (e.target === lb || e.target.classList.contains('lightbox__x')) lb.close(); });
  }

  // Store picker (Call / Directions without hardcoding one shop)
  const picker = $('#picker');
  if (picker) {
    const title = $('#picker-title', picker);
    $$('[data-pick]').forEach(b => b.addEventListener('click', () => {
      const mode = b.dataset.pick;
      picker.dataset.mode = mode;
      title.textContent = title.dataset[mode] || 'Which store?';
      picker.showModal();
    }));
    picker.addEventListener('click', e => {
      if (e.target === picker || e.target.closest('.picker__x') || e.target.closest('.picker__all')) picker.close();
    });
  }

  // Find my nearest store (browser-only geolocation, nothing sent anywhere)
  const nearBtn = $('#near-btn'), list = $('#stores'), status = $('#near-status');
  if (nearBtn && list) {
    const km = (a, b, c, d) => { const r = x => x * Math.PI / 180, R = 6371;
      const h = Math.sin(r(c - a) / 2) ** 2 + Math.cos(r(a)) * Math.cos(r(c)) * Math.sin(r(d - b) / 2) ** 2;
      return 2 * R * Math.asin(Math.sqrt(h)); };
    nearBtn.addEventListener('click', () => {
      if (!navigator.geolocation) { status.textContent = 'Your browser can’t share location. Pick the town closest to you below.'; return; }
      status.textContent = 'Finding you…';
      navigator.geolocation.getCurrentPosition(pos => {
        const { latitude: la, longitude: lo } = pos.coords;
        const cards = $$('.store', list).map(c => ({ c, d: km(la, lo, +c.dataset.lat, +c.dataset.lon) * 0.621371 }));
        cards.sort((x, y) => x.d - y.d).forEach(({ c, d }, i) => {
          list.appendChild(c);
          const tag = $('.store__dist', c); tag.hidden = false; tag.textContent = (i === 0 ? 'Nearest · ' : '') + Math.round(d) + ' mi';
          c.classList.toggle('is-nearest', i === 0);
        });
        const n = cards[0];
        status.textContent = `Closest to you: ${$('h3', n.c).textContent}, about ${Math.round(n.d)} miles away.`;
      }, () => { status.textContent = 'No worries. Location is off, so pick the town closest to you below.'; }, { timeout: 10000, maximumAge: 600000 });
    });
  }

  const yr = $('#yr'); if (yr) yr.textContent = new Date().getFullYear();
})();
