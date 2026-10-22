# Smokes on the Water (4 Wisconsin locations): redesign mockup

Static site: brand homepage (index.html), Locations page (locations/index.html) and one page per store (locations/stoughton.html, beaver-dam.html, horicon.html, oregon.html). Shared CSS/JS in css/ and js/; real store photos from the current Wix site in img/ (WebP).

**Pages are generated.** Edit store data and templates in `src/build.py` (shared sections live in `src/partials/`), then run `python3 src/build.py` to rewrite the HTML files. Commit the generated HTML; Vercel serves it as-is.
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


## Chain restructure (Oct 2026): store data sources
All four store pages on smokesonthewaterwi.com (/stoughton, /beaver-dam, /horicon, /copy-of-stoughton = Oregon) list address, phone, email, Facebook/Yelp/Google links and hours (Mon–Sun 10am–9pm). Cross-checked against Google Maps place cards (all four resolve to "Smokes on the Water" at the same addresses) and third-party listings:
- Stoughton: 233 W Main St, 53589, (608) 205-6868, smokesonthewater.st@gmail.com. "Our second location". Opened Nov 2017 (Stoughton News, 2018).
- Beaver Dam: 501 N Spring St, 53916, (920) 219-9580, smokesonthewater.bd@gmail.com. "Since 2017" (Nextdoor); first shop (news article). Hours confirmed by Waze/Roadtrippers/Loc8NearMe.
- Horicon: 309 E Lake St, 53032, (920) 643-7155, email listed on the official page is the Beaver Dam address (smokesonthewater.bd@gmail.com). "Since 2022" (official page). Phone confirmed by LocalityBiz/MapQuest.
- Oregon: 201 Janesville St, 53575, (608) 608-1081, smokesonthewater.or@gmail.com. Opened Feb 2025 (official page); hours/phone confirmed by Oregon WI Guide, Fivestars, Shisha.com.
- Coordinates: OpenStreetMap Nominatim geocodes of each address (used for "find my nearest store").

## To confirm with the owner
- Horicon hours: official site says 10am–9pm daily; LocalityBiz (Google-derived) shows 11am–9pm. Site uses the official hours.
- Horicon email: official page lists the Beaver Dam inbox; confirm whether Horicon has its own.
- Oregon has no Yelp link on the official page; omitted.
- Wix homepage/About still say "three locations"; the redesign says four (Oregon page confirms the fourth).
- Accessibility/payment details are only verified for Stoughton (Google listing).
- An old Beaver Dam address (135 Front St) and phone (920) 219-4186 appear on Cannapages; treated as outdated.
