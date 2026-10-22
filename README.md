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


## Pen menu section (#pens) image sources
- Half Bak'd (official, half-bakd.com): Angel Food 4G Sativa Disposable (SAUCE'D Exotix), https://half-bakd.com/cdn/shop/files/Dispo_angel_food_02_bd2309b8-27cd-4c56-ae39-d40aa40c993c.png ; Pink Picasso 4G Hybrid Disposable, https://half-bakd.com/cdn/shop/files/Pink_piccaso_02.png
- Twenty One Cannabis (official, twentyonecannabis.com): THCa 1ml Vape Cartridge, Black Lime (Indica), https://twentyonecannabis.com/wp-content/uploads/2024/10/black-lime-front-21-THCa-1ml-cart-9.99.webp ; Cookie Monster (Indica), https://twentyonecannabis.com/wp-content/uploads/2024/10/cookie-monster-front-21-THCa-1ml-cart-9.99.webp
- The 21 cart photos are cropped just below the box's printed price banner (brand, strain, THCa and volume stay visible).

## Hero day/night
Uses the stores' own photos from the Wix site: Oregon storefront (img/loc-oregon-1.webp, day) and Stoughton storefront (img/storefront-night.webp, night). Captions: "Stocked by day." / "Smokin' by night."


## Chain restructure (Oct 2026): store data sources
All four store pages on smokesonthewaterwi.com (/stoughton, /beaver-dam, /horicon, /copy-of-stoughton = Oregon) list address, phone, email, Facebook/Yelp/Google links and hours (Mon–Sun 10am–9pm). Cross-checked against Google Maps place cards (all four resolve to "Smokes on the Water" at the same addresses) and third-party listings:
- Stoughton: 233 W Main St, 53589, (608) 205-6868, smokesonthewater.st@gmail.com. "Our second location". Opened Nov 2017 (Stoughton News, 2018).
- Beaver Dam: 501 N Spring St, 53916, (920) 219-9580, smokesonthewater.bd@gmail.com. "Since 2017" (Nextdoor); first shop (news article). Hours corroborated by Waze/Roadtrippers/Loc8NearMe.
- Horicon: 309 E Lake St, 53032, (920) 643-7155, smokesonthewater.bd@gmail.com (as listed on the official page). "Since 2022" (official page). Phone corroborated by LocalityBiz/MapQuest and the store's Facebook page.
- Oregon: 201 Janesville St, 53575, (608) 608-1081, smokesonthewater.or@gmail.com. Opened Feb 2025 (official page); hours/phone corroborated by Oregon WI Guide, Fivestars, Shisha.com.
- Coordinates: OpenStreetMap Nominatim geocodes of each address (used for "find my nearest store").

## Decisions log (Oct 22, 2026)
- **Horicon hours: 10am–9pm daily.** Source: official store page (smokesonthewaterwi.com/horicon). The store's Facebook page lists no hours (latest post Sep 1, 2025: "Open For Business"); Google Maps shows no hours because the listing is flagged "Permanently closed"; LocalityBiz's 11am–9pm is an older scrape. Horicon stays listed because the business's own site lists it as an active shop.
- **Horicon email: smokesonthewater.bd@gmail.com.** Source: official Horicon page.
- **Location count: four.** Source: official store pages (Oregon page: "our fourth location"); the Wix homepage's "three locations" text predates Oregon.
- **Accessibility: wheelchair-accessible entrance and parking lot at all four shops.** Source: Google Maps "About" tab for each listing (checked Oct 22, 2026).
- **Payments: credit, debit and tap-to-pay listed for Stoughton only.** Source: Stoughton Google listing; not shown for the other three, so not claimed.
- **Old Beaver Dam address (135 Front St / 920-219-4186): excluded.** Source: appears only on Cannapages; every current listing uses 501 N Spring St.
- **Google ratings: not hardcoded.** Each store links to its own Google reviews ("Read our Google reviews"), using the review links from the official store pages.
- **Pens: "stock varies by shop" copy and pricing fine print kept; printed $9.99 cropped out of the 21 Cannabis box photos.**
- **Newsletter form: removed.** It had no backend; replaced with a "Follow @smokesonthewaterwi" Instagram call to action.
- **Loyalty program: not mentioned.** It isn't described on the business's own site or socials. A customer review that mentioned it was swapped for another real Stoughton Yelp review (Murray M.).
- **Nicotine warning:** "WARNING: This product contains nicotine. Nicotine is an addictive chemical." in the footer of every page.
- **Lightbox:** the viewer image is created on first open, so pages no longer contain an empty image.
- **Screenshots:** all regenerated for the chain version; screenshots/before/ holds the original Wix site for comparison.

