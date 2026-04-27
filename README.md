# Airbnb Scraper — Occupancy Rate, ADR & RevPAR (Apify Actor)

Scrape **[Airbnb](https://www.airbnb.com)** listings at scale and get the short-term-rental metrics that actually matter: **occupancy rate, ADR (Average Daily Rate), RevPAR (Revenue Per Available Room)**, plus a forward-looking 12-month booking calendar, host portfolio, reviews, photos, amenities and pricing.

> 👉 Run it on Apify (no install): **[apify.com/hotels-scrapers/airbnb-scraper](https://apify.com/hotels-scrapers/airbnb-scraper)**

This repository is a minimal **Python example** showing how to invoke the deployed Actor through the Apify API and pull structured results.

## What this Airbnb scraper extracts

| Field | Description |
|---|---|
| `listingId` | Airbnb room ID |
| `title` | Listing headline |
| `city` / `country` | Location |
| `occupancyRate` | Booked-nights ÷ available-nights over the 12-month window |
| `ADR` | Average Daily Rate (currency configurable) |
| `RevPAR` | Revenue Per Available Room |
| `calendar` | Day-by-day booked / blocked / price for the next 12 months |
| `reviewsCount` | Total reviews |
| `host` | Host id, name, superhost flag, optional full portfolio |
| `amenities`, `images`, `coordinates` | Standard listing detail |

## Quick start — Python example

```bash
git clone https://github.com/everythingscraper/airbnb-scraper.git
cd airbnb-scraper
pip install -r requirements.txt
export APIFY_TOKEN=your_apify_token   # https://console.apify.com/settings/integrations
python main.py
```

`main.py` runs a 10-listing search for Paris, prints occupancy/ADR/RevPAR for the first 5 hits, and links the full dataset.

## How to scrape Airbnb — input options

Two modes:

- **`mode: "search"`** — provide `location`, `checkIn`, `checkOut`. Optionally `currency`, `maxListings` (1–200).
- **`mode: "direct"`** — provide an array of `listingUrls` (`https://www.airbnb.com/rooms/...`).

Optional flags:

- `includeReviews` — fetch reviews per listing.
- `includeHostPortfolio` — fetch every other listing the host operates (great for STR investor research).
- `proxyConfiguration` — residential is required to clear Airbnb's WAF.

Full input schema: **[Input tab on Apify](https://apify.com/hotels-scrapers/airbnb-scraper/input-schema)**.

## Sample output

```json
{
  "listingId": "53412345",
  "title": "Sunny 1BR near Eiffel Tower",
  "city": "Paris",
  "occupancyRate": 0.78,
  "ADR": 142.50,
  "RevPAR": 111.15,
  "reviewsCount": 312,
  "host": {"id": "98765", "isSuperhost": true},
  "scrapedAt": "2026-04-27T10:00:00Z"
}
```

Datasets export as **JSON, CSV, Excel, HTML, or XML**.

## How much does it cost to scrape Airbnb?

Pay-per-result: **$0.005 per listing**. The Apify Free plan ($5 platform credit) covers ≈ 1,000 Airbnb listings. The Starter plan ($49/mo) covers ≈ 9,800 listings. Adding `includeReviews` or `includeHostPortfolio` increases CU consumption proportionally.

## FAQ

**Why use this instead of Airbnb's official API?**
Airbnb does not offer a public listings API. This Actor is the supported alternative for STR analytics, market research, and pricing intelligence.

**How is `occupancyRate` calculated?**
`booked_nights / available_nights` across the 12-month forward calendar (matches AirDNA / Mashvisor methodology).

**Are reviews and host data included?**
Reviews are off by default (`includeReviews: false`) to save credits. Host portfolio (`includeHostPortfolio`) lets you map an entire operator across cities.

**What proxy do I need?**
Residential. Airbnb's WAF blocks datacenter IPs. The default `apifyProxyGroups: ["RESIDENTIAL"]` is correct for most regions.

**Can I scrape historical occupancy?**
The Airbnb calendar only exposes forward 12 months. For historical, snapshot the dataset on a schedule and roll up over time.

**Need a different field or a custom run?**
Open an issue or contact us via the [Apify Actor page](https://apify.com/hotels-scrapers/airbnb-scraper).

## Other Apify Actors by everythingscraper

- 🏢 **[LoopNet Scraper](https://github.com/everythingscraper/loopnet-scraper)** — commercial real estate listings
- 🏨 **[Trip.com Hotel Scraper](https://github.com/everythingscraper/trip-hotel-scraper)** — hotel pricing across 51 countries
- 🏖️ **[Traveloka Hotel Scraper](https://github.com/everythingscraper/traveloka-hotel-scraper)** — Southeast Asia hotel data

## Is it legal to scrape Airbnb?

This Actor extracts only publicly visible Airbnb data — listings, prices, public reviews, and public host info. It does not bypass logins or extract private user data. Personal data appearing in scraped results is protected by GDPR and similar laws. Use legitimately (market research, STR analytics) and consult your lawyers if unsure.

## License

MIT — see [LICENSE](./LICENSE).
