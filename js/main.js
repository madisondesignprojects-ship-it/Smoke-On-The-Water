(() => {
  // Age gate (remembered for 30 days)
  const gate = document.getElementById('gate');
  const ok = Number(localStorage.getItem('sotw21') || 0) > Date.now();
  if (!ok && !/[?&]nogate/.test(location.search)) {
    gate.hidden = false; document.body.style.overflow = 'hidden';
    document.getElementById('gate-yes').focus();
  }
  document.getElementById('gate-yes').addEventListener('click', () => {
    localStorage.setItem('sotw21', Date.now() + 30 * 864e5);
    gate.hidden = true; document.body.style.overflow = '';
  });

  // Mobile menu
  const burger = document.getElementById('burger'), nav = document.getElementById('nav');
  const setNav = (open) => { nav.classList.toggle('open', open); burger.setAttribute('aria-expanded', open); burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu'); };
  burger.addEventListener('click', () => setNav(!nav.classList.contains('open')));
  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setNav(false)));
  document.addEventListener('keydown', e => { if (e.key === 'Escape') setNav(false); });

  // Open-now status + today's hours (store time: America/Chicago, 10am–9pm daily)
  const parts = new Intl.DateTimeFormat('en-US', { timeZone: 'America/Chicago', weekday: 'short', hour: 'numeric', hour12: false }).formatToParts(new Date());
  const wd = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'].indexOf(parts.find(p => p.type === 'weekday').value);
  const hr = Number(parts.find(p => p.type === 'hour').value) % 24;
  const open = hr >= 10 && hr < 21;
  const s = document.getElementById('open-status');
  s.textContent = open ? 'Open now until 9pm' : (hr < 10 ? 'Closed now · Opens today at 10am' : 'Closed now · Opens tomorrow at 10am');
  if (!open) s.closest('.topbar').classList.add('closed');
  const row = document.querySelector(`#hours tr[data-d="${wd}"]`); if (row) row.classList.add('today');

  // Lightbox
  const lb = document.getElementById('lightbox'), lbImg = lb.querySelector('img');
  document.querySelectorAll('.g').forEach(b => b.addEventListener('click', () => {
    const i = b.querySelector('img'); lbImg.src = b.dataset.full; lbImg.alt = i.alt; lb.showModal();
  }));
  lb.addEventListener('click', e => { if (e.target === lb || e.target.classList.contains('lightbox__x')) lb.close(); });

  document.getElementById('yr').textContent = new Date().getFullYear();
})();
