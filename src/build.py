#!/usr/bin/env python3
"""Static site generator for the Smokes on the Water chain site.
Run: python3 src/build.py  -> writes index.html, locations/index.html, locations/<slug>.html
All store facts below come from smokesonthewaterwi.com store pages (see README for sources)."""
import json, os, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda n: open(os.path.join(ROOT, 'src/partials', n)).read()
SITE = 'https://smoke-on-the-water.vercel.app/'
E = html.escape

STORES = [
 dict(slug='stoughton', town='Stoughton', street='233 W Main Street', street_short='233 W Main St', zip='53589',
      phone='(608) 205-6868', tel='+16082056868', email='smokesonthewater.st@gmail.com',
      lat=42.91660, lon=-89.22248, since='Opened Nov 2017', since_year='2017',
      fb='https://www.facebook.com/smokesonthewaterthedeuce/', yelp='https://www.yelp.com/biz/smokes-on-the-water-stoughton-4',
      tagline='Three floors on the Yahara River',
      blurb='Our second shop sits in Stoughton&rsquo;s historic downtown, easy to reach from Main Street, with a gorgeous view over the Yahara River and quaint shops, local eateries and museums all around.',
      more='Street level has an extensive selection of devices and accessories, a nic juice bar, hundreds of disposable nicotine and Delta options, concentrates, edibles and exotic snacks. Upstairs: a killer glass selection, torches, ashtrays and maintenance supplies. Downstairs: incense, candles, detox, CBD, house-made jewelry, apparel and so much more.',
      amen=['&#9855; Wheelchair-accessible entrance', '&#127359;&#65039; Accessible parking lot', '&#128179; Credit, debit &amp; tap-to-pay', '&#129706; 21+ with valid ID'],
      greviews='https://www.google.com/search?q=smokes+on+the+water+stoughton+wi#lrd=0x88064643d06f622d:0xe3076a142ee1569f,1,,,,',
      cover='storefront-day-2', photos=[('storefront-night','Storefront glowing at night'),('interior-counter','Main floor display counters'),('welcome-snacks','Wall of disposables and e-liquid'),('storefront-night-wide','Lit glass display cases'),('glass-case','Welcome sign over the snacks and drinks coolers'),('interior-accessories','Accessories and gifts display'),('vape-wall','Vape devices and pods wall'),('disposables-wall','The storefront from the street at night')]),
 dict(slug='beaver-dam', town='Beaver Dam', street='501 N Spring Street', street_short='501 N Spring St', zip='53916',
      phone='(920) 219-9580', tel='+19202199580', email='smokesonthewater.bd@gmail.com',
      lat=43.46065, lon=-88.83668, since='Since 2017', since_year='2017',
      fb='https://www.facebook.com/SmokesonthewaterBD/', greviews='https://www.google.com/search?q=smokes+on+the+water+beaver+dam+wi#lrd=0x88069f13abe8092f:0x617701e6f30dde8a,1,,,,', yelp='https://www.yelp.com/biz/smokes-on-the-water-beaver-dam',
      tagline='Where it all started',
      blurb='Smokes on the Water BD sits in the heart of Beaver Dam, a city known for its lake and lively community, surrounded by local businesses. The original Smokes on the Water, serving Beaver Dam since 2017.',
      more='A broad spectrum of products and a staff with a wealth of knowledge make this shop a hub for the local vaping community, whether you&rsquo;re a seasoned vaper or just getting started.',
      amen=['&#9855; Wheelchair-accessible entrance', '&#127359;&#65039; Accessible parking lot', '&#129706; 21+ with valid ID'],
      cover='loc-beaver-dam-1', photos=[('loc-beaver-dam-2','Disposables and display cases'),('loc-beaver-dam-3','Main counter and back-wall shelving'),('loc-beaver-dam-4','Displays and coolers'),('loc-beaver-dam-5','Sales floor with product tower')]),
 dict(slug='horicon', town='Horicon', street='309 E Lake Street', street_short='309 E Lake St', zip='53032',
      phone='(920) 643-7155', tel='+19206437155', email='smokesonthewater.bd@gmail.com',
      lat=43.45145, lon=-88.63227, since='Since 2022', since_year='2022',
      fb='https://www.facebook.com/SOWhoricon', greviews='https://www.google.com/search?q=smokes+on+the+water+horicon+wi#lrd=0x88043d3281b61175:0x9b3713f42a54612c,1,,,,', yelp='https://www.yelp.com/biz/smokes-on-the-water-horicon',
      tagline='Dodge County&rsquo;s neighborhood shop',
      blurb='The go-to smoke shop in Horicon since 2022. From vapes and e-juice to tobacco products and jewelry, there&rsquo;s something for everyone.',
      more='We&rsquo;re dedicated to giving Horicon, Dodge County and the surrounding area exceptional customer service and quality products at affordable prices. Stop in and check it out.',
      amen=['&#9855; Wheelchair-accessible entrance', '&#127359;&#65039; Accessible parking lot', '&#129706; 21+ with valid ID'],
      cover='loc-horicon-1', photos=[('loc-horicon-2','Display counter and shelving'),('loc-horicon-3','Glass and accessories cases'),('loc-horicon-4','Apparel and accessories wall'),('loc-horicon-5','Lit display cases')]),
 dict(slug='oregon', town='Oregon', street='201 Janesville Street', street_short='201 Janesville St', zip='53575',
      phone='(608) 608-1081', tel='+16086081081', email='smokesonthewater.or@gmail.com',
      lat=42.92528, lon=-89.38319, since='Opened Feb 2025', since_year='2025',
      fb='https://www.facebook.com/profile.php?id=61572636715172', greviews='https://www.google.com/search?q=smokes+on+the+water+oregon+wi#lrd=0x88064b86d458c10b:0xb63d3913a06e5fb1,1,,,,', yelp=None,
      tagline='The newest shop in the family',
      blurb='Our fourth location opened in February 2025 at 201 Janesville Street in beautiful downtown Oregon.',
      more='Vapes, legal hemp, edibles, glass, accessories, gifts and more, with the same friendly, knowledgeable crew you&rsquo;ll find at every Smokes on the Water.',
      amen=['&#9855; Wheelchair-accessible entrance', '&#127359;&#65039; Accessible parking lot', '&#129706; 21+ with valid ID'],
      cover='loc-oregon-1', photos=[('loc-oregon-2','Sales floor and entry mat'),('loc-oregon-3','Disposable vape wall'),('loc-oregon-4','Product tower by the entrance'),('loc-oregon-5','Lit vape display cases')]),
]
for s in STORES:
    s['city'] = f"{s['town']}, WI {s['zip']}"
    q = f"{s['street_short']} {s['town']} WI {s['zip']}".replace(' ', '+')
    s['dir'] = f"https://www.google.com/maps/dir/?api=1&amp;destination={q}"
    s['gmap'] = f"https://www.google.com/maps/search/?api=1&amp;query=Smokes+on+the+Water+{q}"
    s['embed'] = f"https://maps.google.com/maps?q=Smokes+on+the+Water,+{q}&amp;z=16&amp;output=embed"

IG = 'https://www.instagram.com/smokesonthewaterwi/'
SVG = {
 'phone': '<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>',
 'pin': '<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 1 7 7c0 5.2-7 13-7 13S5 14.2 5 9a7 7 0 0 1 7-7zm0 4.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5z"/></svg>',
 'cart': '<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M7 4h-2l-1 2v1h2l3.6 7.6-1.4 2.4A2 2 0 0 0 10 20h10v-2H10l1.1-2h7.4a2 2 0 0 0 1.8-1.1L23 8H7.2zM10 21a1.5 1.5 0 1 0 0 .01zM19 21a1.5 1.5 0 1 0 0 .01z"/></svg>',
 'locate': '<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8zm9 3h-2.06A7 7 0 0 0 13 5.06V3h-2v2.06A7 7 0 0 0 5.06 11H3v2h2.06A7 7 0 0 0 11 18.94V21h2v-2.06A7 7 0 0 0 18.94 13H21zm-9 6a5 5 0 1 1 0-10 5 5 0 0 1 0 10z"/></svg>',
 'ig': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 2h10a5 5 0 0 1 5 5v10a5 5 0 0 1-5 5H7a5 5 0 0 1-5-5V7a5 5 0 0 1 5-5zm0 2a3 3 0 0 0-3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3-3V7a3 3 0 0 0-3-3zm5 3.5a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9zm0 2a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM17.5 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/></svg>',
}
FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230b0d0a'/%3E%3Cpath d='M14 40c6-6 12 6 18 0s12 6 18 0' stroke='%23c8f53c' stroke-width='5' fill='none' stroke-linecap='round'/%3E%3Cpath d='M24 28c-4-5 4-8 0-13M34 28c-4-5 4-8 0-13' stroke='%23fff' stroke-width='3.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E"

def store_ld(s):
    d = {"@type": "Store", "@id": SITE + f"locations/{s['slug']}.html#store",
         "name": f"Smokes on the Water - {s['town']}", "url": SITE + f"locations/{s['slug']}.html",
         "image": SITE + f"img/{s['cover']}.webp", "telephone": '+1-' + s['tel'][2:5] + '-' + s['tel'][5:8] + '-' + s['tel'][8:],
         "email": s['email'], "priceRange": "$$",
         "address": {"@type": "PostalAddress", "streetAddress": s['street_short'], "addressLocality": s['town'], "addressRegion": "WI", "postalCode": s['zip'], "addressCountry": "US"},
         "geo": {"@type": "GeoCoordinates", "latitude": s['lat'], "longitude": s['lon']},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], "opens": "10:00", "closes": "21:00"}],
         "sameAs": [u for u in [s['fb'], s['yelp'], IG] if u],
         "parentOrganization": {"@id": SITE + "#org"}}
    d.pop('priceRange')
    return d

ORG = {"@type": "Organization", "@id": SITE + "#org", "name": "Smokes on the Water", "url": SITE,
       "logo": SITE + "img/logo-wordmark.png", "foundingDate": "2017", "sameAs": [IG, "https://www.smokesonthewaterwi.com/"]}

def jsonld(items):
    return '<script type="application/ld+json">\n' + json.dumps({"@context": "https://schema.org", "@graph": items}, indent=1, ensure_ascii=False) + '\n</script>'

def head(title, desc, path, og, ld, R):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Smokes on the Water">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}img/{og}.webp">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b0d0a">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{R}css/styles.css">
{ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<!-- Age gate (21+), same rule the current site enforces -->
<div class="gate" id="gate" role="dialog" aria-modal="true" aria-labelledby="gate-title" hidden>
  <div class="gate__card">
    <img src="{R}img/logo-wordmark.png" alt="Smokes on the Water" width="293" height="32">
    <h2 id="gate-title">Are you 21 or older?</h2>
    <p>You must be 21+ to browse our shops. We check ID at the door at all four Wisconsin locations, every time.</p>
    <div class="gate__btns">
      <button class="btn btn--lime" id="gate-yes">Yes, I'm 21+</button>
      <a class="btn btn--ghost" href="https://www.google.com">No, take me back</a>
    </div>
  </div>
</div>
'''

def header(R, home, store=None):
    a = '' if home else f'{R}index.html'
    loc_link = f'{R}locations/'
    if store:
        cta = f'<a class="btn btn--lime btn--sm header__call" href="tel:{store["tel"]}">{SVG["phone"]}{store["phone"]}</a>'
    else:
        cta = f'<a class="btn btn--lime btn--sm header__call" href="{loc_link}">{SVG["pin"]}Find a store</a>'
    return f'''
<div class="topbar">
  <p><span class="dot"></span> <span id="open-status">Open daily 10am–9pm</span> <span class="sep">·</span> <a href="{loc_link}">4 Wisconsin locations</a> <span class="sep">·</span> <span class="ship">Free shipping on online orders over $100</span></p>
</div>

<header class="header" id="top">
  <div class="wrap header__in">
    <a href="{R}index.html" class="brand" aria-label="Smokes on the Water home">
      <img src="{R}img/logo-wordmark.png" alt="Smokes on the Water" width="293" height="32">
      <span class="brand__loc">{store["town"] + ", WI" if store else "Wisconsin · 4 locations"}</span>
    </a>
    <nav class="nav" id="nav" aria-label="Main">
      <a href="{loc_link}"{' aria-current="page"' if (not home and not store) else ''}>Locations</a>
      <a href="{a}#pens">Pens</a>
      <a href="{a}#shop">Shop</a>
      <a href="{a}#story">Our Story</a>
      <a href="{a}#reviews">Reviews</a>
      <a href="{a}#faq">FAQ</a>
      <a class="nav__cta" href="https://www.smokesonthewaterwi.com/shop">Shop Online</a>
    </nav>
    {cta}
    <button class="burger" id="burger" aria-controls="nav" aria-expanded="false" aria-label="Open menu"><span></span><span></span><span></span></button>
  </div>
</header>
'''

def picker(R):
    rows = ''.join(f'''
      <li class="picker__row">
        <div><strong>{s["town"]}</strong><span>{s["street_short"]}</span></div>
        <a class="btn btn--lime btn--sm" data-mode="call" href="tel:{s["tel"]}">{SVG["phone"]}{s["phone"]}</a>
        <a class="btn btn--lime btn--sm" data-mode="dir" href="{s["dir"]}" target="_blank" rel="noopener">{SVG["pin"]}Directions</a>
      </li>''' for s in STORES)
    return f'''
<dialog class="picker" id="picker" aria-labelledby="picker-title">
  <div class="picker__card">
    <button class="picker__x" type="button" aria-label="Close">×</button>
    <p class="eyebrow">Pick your shop</p>
    <h2 id="picker-title" data-call="Who do you want to call?" data-dir="Where are you headed?">Which store?</h2>
    <ul class="picker__list">{rows}
    </ul>
    <a class="picker__all" href="{R}locations/">See all locations, hours &amp; maps →</a>
  </div>
</dialog>'''

def footer(R, store=None):
    shops = ''.join(f'<li><a href="{R}locations/{s["slug"]}.html">{s["town"]}</a><span>{s["street_short"]}</span><a href="tel:{s["tel"]}">{s["phone"]}</a></li>' for s in STORES)
    if store:
        bar = f'''<nav class="actionbar" aria-label="Quick actions">
  <a href="tel:{store["tel"]}">{SVG["phone"]}Call</a>
  <a href="{store["dir"]}" target="_blank" rel="noopener">{SVG["pin"]}Directions</a>
  <a class="actionbar__main" href="https://www.smokesonthewaterwi.com/shop">{SVG["cart"]}Shop</a>
</nav>'''
    else:
        bar = f'''<nav class="actionbar" aria-label="Quick actions">
  <button type="button" data-pick="call">{SVG["phone"]}Call</button>
  <button type="button" data-pick="dir">{SVG["pin"]}Directions</button>
  <a class="actionbar__main" href="https://www.smokesonthewaterwi.com/shop">{SVG["cart"]}Shop</a>
</nav>'''
    return f'''
<footer class="footer">
  <div class="wrap footer__in">
    <div>
      <img src="{R}img/logo-wordmark.png" alt="Smokes on the Water" width="220" height="24" loading="lazy">
      <p class="muted">Vapes, glass, legal hemp &amp; Delta, CBD, jewelry and gifts. Four Wisconsin shops since 2017: Beaver Dam, Stoughton, Horicon and Oregon.</p>
      <p class="muted">Open daily 10am–9pm.</p>
      <a class="ig" href="{IG}" target="_blank" rel="noopener" aria-label="Smokes on the Water on Instagram">{SVG["ig"]}</a>
    </div>
    <div><h4>Our shops</h4><ul class="fshops">{shops}</ul></div>
    <nav aria-label="Footer"><h4>Shop</h4><a href="https://www.smokesonthewaterwi.com/shop">Shop online</a><a href="https://www.smokesonthewaterwi.com/all-products">All products</a><a href="https://www.smokesonthewaterwi.com/shipping-returns">Shipping &amp; Returns</a><a href="https://www.smokesonthewaterwi.com/copy-of-terms-conditions">Terms &amp; Conditions</a><a href="{R}locations/">All locations</a></nav>
  </div>
  <div class="wrap legal">
    <p><strong>WARNING:</strong> This product contains nicotine. Nicotine is an addictive chemical.</p>
    <p>For sale to adults 21+ only. Valid ID required for every purchase.</p>
    <p><strong>FDA Disclaimer:</strong> The statements made within this website have not been evaluated by the Food and Drug Administration. These statements and the products of this company are not intended to diagnose, treat, cure or prevent any disease.</p>
    <p class="muted">© <span id="yr">2026</span> Smokes on the Water. All rights reserved.</p>
  </div>
</footer>

{bar}
{picker(R)}

<dialog class="lightbox" id="lightbox" aria-label="Photo viewer"><button class="lightbox__x" aria-label="Close">×</button></dialog>

<script src="{R}js/main.js" defer></script>
</body>
</html>
'''

def store_card(s, R):
    return f'''
      <article class="store" data-lat="{s["lat"]}" data-lon="{s["lon"]}" data-slug="{s["slug"]}">
        <a class="store__img" href="{R}locations/{s["slug"]}.html" tabindex="-1" aria-hidden="true"><img src="{R}img/{s["cover"]}-sm.webp" alt="" loading="lazy"><span class="store__since">{s["since"]}</span><span class="store__dist" hidden></span></a>
        <div class="store__body">
          <h3><a href="{R}locations/{s["slug"]}.html">{s["town"]}</a></h3>
          <p class="store__tag">{s["tagline"]}</p>
          <p class="store__addr">{s["street"]}<br>{s["city"]}</p>
          <p class="store__hours"><span class="dot"></span> Open daily 10am–9pm</p>
          <a class="store__tel" href="tel:{s["tel"]}">{SVG["phone"]}{s["phone"]}</a>
          <a class="store__rev" href="{s["greviews"]}" target="_blank" rel="noopener">&#9733; Read our Google reviews</a>
          <div class="store__btns">
            <a class="btn btn--lime btn--sm" href="{s["dir"]}" target="_blank" rel="noopener">Directions</a>
            <a class="btn btn--ghost btn--sm" href="{R}locations/{s["slug"]}.html">Store page →</a>
          </div>
        </div>
      </article>'''

def finder(R, h2, sub, eyebrow='Find your shop', cls='section', sid='locations'):
    cards = ''.join(store_card(s, R) for s in STORES)
    return f'''
<!-- LOCATIONS / STORE FINDER -->
<section class="{cls}" id="{sid}">
  <div class="wrap">
    <div class="finder__head">
      <div class="section__head">
        <p class="eyebrow">{eyebrow}</p>
        <h2>{h2}</h2>
        <p class="muted">{sub}</p>
      </div>
      <div class="finder__tools">
        <button class="btn btn--lime" type="button" id="near-btn">{SVG["locate"]}Find my nearest store</button>
        <p class="finder__status muted" id="near-status" role="status">We only use your location in your browser to sort the list. It&rsquo;s never sent or saved.</p>
      </div>
    </div>
    <div class="stores" id="stores">{cards}
    </div>
  </div>
</section>
'''

REVIEWS = '''
<!-- REVIEWS (real quotes from public review listings) -->
<section class="section section--alt" id="reviews">
  <div class="wrap">
    <div class="section__head">
      <p class="eyebrow">Word around Wisconsin</p>
      <h2>Real reviews from <span class="lime">real regulars</span></h2>
    </div>
    <div class="reviews">
      <figure class="review">
        <div class="stars" aria-label="5 out of 5 stars">★★★★★</div>
        <blockquote>“Really good shop. Every staff member there is very nice, knowledgeable, and professional. Reasonable business practice, good prices, and a vast amount of products… My go-to place for all my smoking needs.”</blockquote>
        <figcaption>Joniahsun · Google review · <a href="{R}locations/stoughton.html">Stoughton</a></figcaption>
      </figure>
      <figure class="review">
        <div class="stars" aria-label="5 out of 5 stars">★★★★★</div>
        <blockquote>“Best shop around hands down. Not going to find another store that is either more informational or more helpful. The crew here not only knows what's up but definitely wants to hook you up with what you want.”</blockquote>
        <figcaption>Codi L. · Google review · <a href="{R}locations/horicon.html">Horicon</a></figcaption>
      </figure>
      <figure class="review">
        <div class="stars" aria-label="5 out of 5 stars">★★★★★</div>
        <blockquote>“Friendly and knowledgeable… tons of choices. Great prices and good operating hours.”</blockquote>
        <figcaption>Murray M. · Yelp · <a href="{R}locations/stoughton.html">Stoughton</a></figcaption>
      </figure>
    </div>
  </div>
</section>
'''

FAQ = '''
<!-- FAQ -->
<section class="section section--alt" id="faq">
  <div class="wrap faq">
    <div class="section__head"><p class="eyebrow">Good to know</p><h2>FAQ</h2></div>
    <details><summary>Do I need an ID?</summary><p>Yes. You must be 21 or older, and we check ID for every purchase at every location.</p></details>
    <details><summary>Where are your stores?</summary><p>Four Wisconsin shops: Beaver Dam (501 N Spring St), Stoughton (233 W Main St), Horicon (309 E Lake St) and Oregon (201 Janesville St). See <a href="{R}locations/">all locations</a> for maps and directions.</p></details>
    <details><summary>What are your hours?</summary><p>All four shops are open every day, 10am–9pm.</p></details>
    <details><summary>Can you order something you don't carry?</summary><p>Usually, yes. We're always expanding our inventory and are happy to bring in items on request. Just ask at the counter or call your local shop.</p></details>
    <details><summary>Do you ship online orders?</summary><p>Yes. Shop online at our store, and orders over $100 ship free. See our <a href="https://www.smokesonthewaterwi.com/shipping-returns">Shipping &amp; Returns</a> policy for details.</p></details>
    <details><summary>Are your shops accessible?</summary><p>Yes. All four shops have a wheelchair-accessible entrance and accessible parking.</p></details>
  </div>
</section>
'''

def gallery(items, R, title='Inside the shops', eyebrow='Take a look', cls='section section--alt'):
    # items: (img, alt, tag, cls)
    btns = ''.join(f'\n      <button class="g {c}" data-full="{R}img/{i}.webp"><img src="{R}img/{i}-sm.webp" alt="{a}" loading="lazy">{f"<span class=g__tag>{t}</span>" if t else ""}</button>' for i, a, t, c in items)
    return f'''
<!-- GALLERY -->
<section class="{cls}" id="gallery">
  <div class="wrap">
    <div class="section__head">
      <p class="eyebrow">{eyebrow}</p>
      <h2>{title}</h2>
    </div>
    <div class="gallery">{btns}
    </div>
  </div>
</section>
'''

def out(path, content):
    full = os.path.join(ROOT, path); os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w').write(content); print('wrote', path)

# ---------------- HOME ----------------
def home():
    R = ''
    t = 'Smokes on the Water | Smoke &amp; Vape Shops in Stoughton, Beaver Dam, Horicon &amp; Oregon, WI'
    d = 'Smokes on the Water: four Wisconsin smoke and vape shops in Beaver Dam, Stoughton, Horicon and Oregon. Vapes, e-liquid, disposables, glass, legal hemp/Delta, CBD, jewelry and gifts. Open daily 10am–9pm. 21+.'
    body = head(t, d, '', 'storefront-night', jsonld([ORG] + [store_ld(s) for s in STORES]), R) + header(R, True) + f'''
<main id="main">
<!-- HERO -->
<section class="hero">
  <div class="hero__smoke" aria-hidden="true"></div>
  <div class="wrap hero__in">
   <div class="hero__copy">
    <p class="eyebrow">Wisconsin-owned · Since 2017</p>
    <h1>Wisconsin's smoke &amp; vape shop, <span class="lime">four towns deep.</span></h1>
    <p class="hero__lead">Vapes, e-liquid, disposables, glass, legal hemp &amp; Delta, CBD, handmade jewelry and gifts in Beaver Dam, Stoughton, Horicon and Oregon, each run by a friendly, knowledgeable crew.</p>
    <div class="hero__ctas">
      <a class="btn btn--lime btn--lg" href="#locations">{SVG["pin"]}Find your store</a>
      <button class="btn btn--ghost btn--lg" type="button" data-pick="call">Call a shop</button>
      <a class="btn btn--text btn--lg" href="https://www.smokesonthewaterwi.com/shop">Shop online →</a>
    </div>
    <ul class="hero__facts">
      <li><strong>4 shops</strong><span>Across Wisconsin</span></li>
      <li><strong>10am–9pm</strong><span>Open 7 days</span></li>
      <li><strong>Since 2017</strong><span>Locally owned</span></li>
      <li><strong>21+</strong><span>ID checked always</span></li>
    </ul>
    <p class="hero__towns"><a href="locations/beaver-dam.html">Beaver Dam</a><a href="locations/stoughton.html">Stoughton</a><a href="locations/horicon.html">Horicon</a><a href="locations/oregon.html">Oregon</a></p>
   </div>
    <div class="daynight" aria-label="Our shops by day and by night">
      <figure class="dn dn--day">
        <img src="img/loc-oregon-1.webp" alt="The Smokes on the Water shop on Janesville Street in Oregon, WI, on a sunny day" fetchpriority="high" width="1400" height="1049">
        <figcaption><span class="dn__icon" aria-hidden="true">☀</span><strong>Stocked by day.</strong><small>Oregon · Doors open 10am</small></figcaption>
      </figure>
      <figure class="dn dn--night">
        <img src="img/storefront-night.webp" alt="The Smokes on the Water storefront in Stoughton at night, its neon windows glowing" fetchpriority="high" width="1340" height="1600">
        <figcaption><span class="dn__icon" aria-hidden="true">☾</span><strong>Smokin&rsquo; by night.</strong><small>Stoughton · Lit till 9pm</small></figcaption>
      </figure>
    </div>
  </div>
  <svg class="wave" viewBox="0 0 1440 80" preserveAspectRatio="none" aria-hidden="true"><path d="M0 40c120-30 240-30 360 0s240 30 360 0 240-30 360 0 240 30 360 0v40H0z"/></svg>
</section>
''' + finder(R, 'Four shops. <span class="lime">Pick yours.</span>', 'Same crew mentality, same 10am–9pm hours, every day of the week. Tap a store for photos, maps and the full scoop.') + P('pens.html').replace('{R}', R) + P('shop.html').replace('{R}', R) + f'''
<!-- STORY -->
<section class="section section--alt" id="story">
  <div class="wrap story">
    <div class="story__img">
      <img src="img/storefront-day.webp" alt="The Smokes on the Water building on W Main St in Stoughton in daylight, with its turret and wraparound deck" loading="lazy">
      <span class="story__badge">Est. 2017</span>
    </div>
    <div class="story__copy">
      <p class="eyebrow">Our story</p>
      <h2>Named for the river (and the riff)</h2>
      <p>Smokes on the Water started in Beaver Dam in 2017. That November we opened shop number two on West Main Street in Stoughton, in a multi-level building on the Yahara River, and the name says it all: a nod to the classic Deep Purple song. Founder Chris Kelley wanted small towns with real demand, and Wisconsin delivered.</p>
      <p>Horicon joined the family in 2022, and Oregon became shop number four in February 2025. The idea hasn&rsquo;t changed: a welcoming, inclusive shop with friendly, knowledgeable staff, competitive prices, and a crew that helps you find exactly what you need, whether you&rsquo;re a seasoned vaper or brand new.</p>
      <ol class="timeline">
        <li><strong>2017</strong><a href="locations/beaver-dam.html">Beaver Dam</a></li>
        <li><strong>Nov 2017</strong><a href="locations/stoughton.html">Stoughton</a></li>
        <li><strong>2022</strong><a href="locations/horicon.html">Horicon</a></li>
        <li><strong>Feb 2025</strong><a href="locations/oregon.html">Oregon</a></li>
      </ol>
      <p class="rules"><strong>Our two house rules:</strong> we check IDs, and we keep it legal.</p>
    </div>
  </div>
</section>
''' + gallery([
        ('storefront-night-wide', 'Lit glass display cases at the Stoughton shop', 'Stoughton', 'g--tall'),
        ('loc-beaver-dam-1', 'Sales floor at the Beaver Dam shop', 'Beaver Dam', 'g--wide'),
        ('loc-horicon-1', 'Shelving and counter at the Horicon shop', 'Horicon', ''),
        ('loc-oregon-3', 'Disposable vape wall at the Oregon shop', 'Oregon', ''),
        ('welcome-snacks', 'Wall of disposables and e-liquid at the Stoughton shop', 'Stoughton', 'g--wide'),
        ('loc-oregon-2', 'Sales floor and Smokes on the Water entry mat in Oregon', 'Oregon', ''),
        ('loc-horicon-3', 'Glass and accessories cases in Horicon', 'Horicon', ''),
        ('loc-beaver-dam-3', 'Main counter and back-wall shelving in Beaver Dam', 'Beaver Dam', ''),
    ], R, 'Inside all four shops', cls='section') + REVIEWS.replace('{R}', R) + P('band.html').replace('{IG}', IG) + FAQ.replace('{R}', R) + '</main>\n' + footer(R)
    out('index.html', body)

# ---------------- LOCATIONS INDEX ----------------
def locations_index():
    R = '../'
    t = 'Locations | Smokes on the Water: 4 Wisconsin Smoke &amp; Vape Shops'
    d = 'Find your nearest Smokes on the Water: Beaver Dam, Stoughton, Horicon and Oregon, WI. Addresses, phone numbers, hours, maps and directions. Open daily 10am–9pm.'
    rows = ''.join(f'''
    <article class="lrow" id="{s["slug"]}">
      <a class="lrow__img" href="{s["slug"]}.html"><img src="../img/{s["cover"]}-sm.webp" alt="Smokes on the Water {s["town"]}" loading="lazy"><span class="store__since">{s["since"]}</span></a>
      <div class="lrow__info">
        <p class="eyebrow">{s["tagline"]}</p>
        <h2><a href="{s["slug"]}.html">{s["town"]}</a></h2>
        <address>{s["street"]}<br>{s["city"]}</address>
        <ul class="contact">
          <li><a href="tel:{s["tel"]}">{s["phone"]}</a></li>
          <li><a href="mailto:{s["email"]}">{s["email"]}</a></li>
          <li class="muted">Open daily 10am–9pm</li>
          <li><a href="{s["greviews"]}" target="_blank" rel="noopener">&#9733; Read our Google reviews</a></li>
        </ul>
        <div class="visit__ctas">
          <a class="btn btn--lime btn--sm" href="{s["dir"]}" target="_blank" rel="noopener">Get directions</a>
          <a class="btn btn--ghost btn--sm" href="tel:{s["tel"]}">Call</a>
          <a class="btn btn--text btn--sm" href="{s["slug"]}.html">Store page →</a>
        </div>
      </div>
      <div class="lrow__map"><iframe title="Map of Smokes on the Water {s["town"]}, {s["street_short"]}" src="{s["embed"]}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
    </article>''' for s in STORES)
    body = head(t, d, 'locations/', 'loc-oregon-1', jsonld([ORG] + [store_ld(s) for s in STORES]), R) + header(R, False) + f'''
<main id="main">
<section class="phead">
  <div class="wrap">
    <p class="crumbs"><a href="../index.html">Home</a> / Locations</p>
    <p class="eyebrow">4 Wisconsin locations</p>
    <h1>Find your <span class="lime">Smokes on the Water.</span></h1>
    <p class="hero__lead">Beaver Dam, Stoughton, Horicon and Oregon. Every shop is open daily 10am–9pm and checks ID at the door.</p>
  </div>
</section>
''' + finder(R, 'Closest shop to you', 'Tap the button and we&rsquo;ll sort the shops by distance.', 'Store finder', 'section section--tight', 'finder') + f'''
<section class="section section--alt" id="all">
  <div class="wrap lrows">{rows}
  </div>
</section>
</main>
''' + footer(R)
    out('locations/index.html', body)

# ---------------- STORE PAGES ----------------
def store_page(s):
    R = '../'
    t = f'Smokes on the Water {s["town"]}, WI | Smoke &amp; Vape Shop at {s["street_short"]}'
    d = f'Smokes on the Water {s["town"]}: smoke and vape shop at {s["street_short"]}, {s["city"]}. Call {s["phone"]}. Open daily 10am–9pm. 21+.'
    days = [('1','Monday'),('2','Tuesday'),('3','Wednesday'),('4','Thursday'),('5','Friday'),('6','Saturday'),('0','Sunday')]
    hours = ''.join(f'<tr data-d="{n}"><th>{dn}</th><td>10am – 9pm</td></tr>' for n, dn in days)
    socials = [f'<li><a href="{s["fb"]}" target="_blank" rel="noopener">Facebook: Smokes on the Water {s["town"]}</a></li>']
    if s['yelp']: socials.append(f'<li><a href="{s["yelp"]}" target="_blank" rel="noopener">Yelp reviews</a></li>')
    socials.insert(0, f'<li><a href="{s["greviews"]}" target="_blank" rel="noopener">&#9733; Read our Google reviews</a></li>')
    socials.append(f'<li><a href="{IG}" target="_blank" rel="noopener">@smokesonthewaterwi on Instagram</a></li>')
    amen = ''.join(f'<li>{a}</li>' for a in s['amen'])
    others = ''.join(f'<li><a href="{o["slug"]}.html"><img src="../img/{o["cover"]}-sm.webp" alt="" loading="lazy"><span><strong>{o["town"]}</strong>{o["street_short"]} · {o["phone"]}</span></a></li>' for o in STORES if o is not s)
    extra = P('floors.html').replace('<h2>Three floors. One historic building.</h2>', '<h2>Three floors. One historic building.</h2>') if s['slug'] == 'stoughton' else ''
    wides = {0, 3} if len(s['photos']) == 4 else {0, 3, 4, 7}
    gal = gallery([(i, f'{a}, Smokes on the Water {s["town"]}', '', 'g--wide' if k in wides else '') for k, (i, a) in enumerate(s['photos'])], R, f'Inside {s["town"]}', 'Photos', 'section')
    if len(s['photos']) == 4: gal = gal.replace('<div class="gallery">', '<div class="gallery gallery--3">')
    body = head(t, d, f'locations/{s["slug"]}.html', s['cover'], jsonld([ORG, store_ld(s)]), R) + header(R, False, s) + f'''
<main id="main">
<section class="lhero">
  <div class="lhero__bg"><img src="../img/{s["cover"]}.webp" alt="" fetchpriority="high"></div>
  <div class="wrap lhero__in">
    <p class="crumbs"><a href="../index.html">Home</a> / <a href="./">Locations</a> / {s["town"]}</p>
    <p class="eyebrow">Smokes on the Water · {s["since"]}</p>
    <h1>{s["town"]}<span class="lime">, WI</span></h1>
    <p class="hero__lead">{s["blurb"]}</p>
    <div class="hero__ctas">
      <a class="btn btn--lime btn--lg" href="tel:{s["tel"]}">{SVG["phone"]}Call {s["phone"]}</a>
      <a class="btn btn--ghost btn--lg" href="{s["dir"]}" target="_blank" rel="noopener">Get Directions</a>
    </div>
  </div>
  <svg class="wave" viewBox="0 0 1440 80" preserveAspectRatio="none" aria-hidden="true"><path d="M0 40c120-30 240-30 360 0s240 30 360 0 240-30 360 0 240 30 360 0v40H0z"/></svg>
</section>

<!-- VISIT -->
<section class="section" id="visit">
  <div class="wrap visit">
    <div class="visit__info">
      <p class="eyebrow">Come see us</p>
      <h2>Visit the {s["town"]} shop</h2>
      <address><strong>{s["street"]}</strong><br>{s["city"]}</address>
      <table class="hours" aria-label="Store hours">
        <tbody id="hours">{hours}</tbody>
      </table>
      <ul class="contact">
        <li><a href="tel:{s["tel"]}">{s["phone"]}</a></li>
        <li><a href="mailto:{s["email"]}">{s["email"]}</a></li>
        {''.join(socials)}
      </ul>
      <ul class="amen">{amen}</ul>
      <div class="visit__ctas">
        <a class="btn btn--lime" href="{s["dir"]}" target="_blank" rel="noopener">Get Directions</a>
        <a class="btn btn--ghost" href="tel:{s["tel"]}">Call the shop</a>
      </div>
    </div>
    <div class="visit__map">
      <iframe title="Map showing Smokes on the Water at {s["street_short"]}, {s["town"]}, WI" src="{s["embed"]}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      <a class="map__link" href="{s["gmap"]}" target="_blank" rel="noopener">Open in Google Maps ↗</a>
    </div>
  </div>
</section>

<section class="section section--alt section--tight">
  <div class="wrap about">
    <p class="eyebrow">About this shop</p>
    <p class="about__lead">{s["more"]}</p>
  </div>
</section>
''' + extra + gal + f'''
<section class="section" id="others">
  <div class="wrap">
    <div class="section__head"><p class="eyebrow">The rest of the family</p><h2>Other Smokes on the Water shops</h2></div>
    <ul class="others">{others}</ul>
    <p style="margin-top:22px"><a class="btn btn--ghost" href="./">All locations &amp; maps</a></p>
  </div>
</section>
</main>
''' + footer(R, s)
    out(f'locations/{s["slug"]}.html', body)

if __name__ == '__main__':
    home(); locations_index()
    for s in STORES: store_page(s)
