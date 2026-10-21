# Smokes on the Water (Stoughton, WI): redesign mockup

Static single-page site: index.html, css/styles.css, js/main.js, img/ (real store photos from the current Wix site, converted to WebP).
Preview: `python3 -m http.server` in this folder, then open http://localhost:8000 (add `?nogate` to skip the 21+ age gate).

## Content sources (all real, nothing invented)
- smokesonthewaterwi.com: Home, /stoughton, /beaver-dam, /horicon, /copy-of-stoughton (Oregon), /about-us, /shop, /all-products, footer FDA disclaimer, 21+ age gate, free shipping over $100
- Nextdoor business page: "happy to bring in items on request", since 2017
- Stoughton News / Unified Newspaper Group, Jun 16 2018: opened Nov 2017, founder Chris Kelley, second shop after Beaver Dam, Deep Purple name nod, "we check IDs and keep it legal"
- Google listing via shisha.com/exa: 4.5★ (~130 reviews), wheelchair-accessible entrance, credit/debit/NFC, Joniahsun review
- Yelp via Yahoo Local: Valerie P. and Murray M. quotes, "near the corner of Page and Main, right on the water"

## Placeholders / to confirm with the owner
- Loyalty program details (only known from a Yelp review); newsletter form is front-end only (no backend)
- Nicotine warning text in the footer is a suggested compliance line; confirm with the owner
- Review count/rating changes over time; pull it live in production
- Map is an OpenStreetMap embed (no API key); swap for a Google Maps embed in production if preferred

## Pen menu section (#pens) image sources
- Half Bak'd (official, half-bakd.com): Angel Food 4G Sativa Disposable (SAUCE'D Exotix), https://half-bakd.com/cdn/shop/files/Dispo_angel_food_02_bd2309b8-27cd-4c56-ae39-d40aa40c993c.png ; Pink Picasso 4G Hybrid Disposable, https://half-bakd.com/cdn/shop/files/Pink_piccaso_02.png
- Twenty One Cannabis (official, twentyonecannabis.com): THCa 1ml Vape Cartridge, Black Lime (Indica), https://twentyonecannabis.com/wp-content/uploads/2024/10/black-lime-front-21-THCa-1ml-cart-9.99.webp ; Cookie Monster (Indica), https://twentyonecannabis.com/wp-content/uploads/2024/10/cookie-monster-front-21-THCa-1ml-cart-9.99.webp
- Confirm with the owner which pens are actually stocked; packaging shows a printed $9.99 MSRP on the 21 carts.

## Hero day/night
Uses the store's own photos from the Wix site: img/storefront-day-2.webp (day) and img/storefront-night.webp (night). Captions: "Stocked by day." / "Smokin' by night."
