# Airbnb Scraper — Occupancy, ADR & RevPAR (Apify Actor)

> Short-term-rental analytics on tap. No AirDNA subscription, no Mashvisor seat, no scraper to maintain.

Extract **[Airbnb](https://www.airbnb.com)** listings with the metrics that actually drive STR underwriting: forward 12-month **occupancy rate**, **ADR** (Average Daily Rate), **RevPAR** (Revenue Per Available Room), full booking calendar, host portfolio, reviews, amenities, and pricing.

🚀 **Try it on Apify** → https://apify.com/hotels-scrapers/airbnb-scraper

This GitHub repo is the **Python how-to** — a tiny `main.py` that calls the deployed Actor, dumps the results to JSON, and prints the market-level mean of occupancy / ADR / RevPAR.

## Built for

- 🏘️ **STR investors** — comp underwriting before you wire EMD
- 📈 **Market analysts** — backfill AirDNA-style reports across cities
- 🏷️ **Pricing engines** — daily comp scrape into your dynamic-pricing model
- 🕵️ **Operator intel** — map a competitor's full host portfolio in one run
- 🏛️ **Tax / regulatory** — quantify Airbnb supply by neighborhood for policy briefs

## What you get back

| Field | Notes |
|---|---|
| `listingId`, `title`, `city`, `country` | Listing identity & geo |
| `occupancyRate` | Booked nights ÷ available nights, 12-month forward |
| `ADR` | Average Daily Rate (currency configurable) |
| `RevPAR` | `occupancyRate × ADR` |
| `calendar` | Day-by-day booked / blocked / price (12 months) |
| `reviewsCount`, `host` | Optional review and host-portfolio expansions |
| `amenities`, `images`, `coordinates` | Standard listing detail |

## Quick start (Python)

```bash
git clone https://github.com/everythingscraper/airbnb-scraper.git
cd airbnb-scraper
pip install -r requirements.txt
APIFY_TOKEN=your_token python main.py
```

`main.py` runs a 10-listing Paris search, writes `airbnb_results.json`, and prints market means. Token: https://console.apify.com/settings/integrations.

## Input — two modes

**`mode: "search"`** → set `location`, `checkIn`, `checkOut`, optional `currency` and `maxListings` (1–200).

**`mode: "direct"`** → pass an array of `listingUrls` (`https://www.airbnb.com/rooms/...`).

Optional toggles:
- `includeReviews` — fetch review text and stars per listing.
- `includeHostPortfolio` — fetch every other listing the same host runs (operator-intel mode).
- `proxyConfiguration` — residential required to clear Airbnb's WAF.

Schema: **[Input tab on Apify](https://apify.com/hotels-scrapers/airbnb-scraper/input-schema)**.

## Sample row

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

Export from Apify Storage as **JSON, CSV, Excel, HTML, or XML**.

## Pricing

**$0.005 per listing** (pay-per-result).

| Plan | ≈ Listings |
|---|---|
| Free ($5 credit) | 1,000 |
| Starter ($49/mo) | 9,800 |
| Scale ($499/mo) | 99,800 |

`includeReviews` and `includeHostPortfolio` increase CU consumption; baseline figures assume both off.

## FAQ

**How does this compare to AirDNA / Mashvisor?**
Same methodology, raw data direct from Airbnb, ~80–95 % cheaper at low-to-mid volumes, fully programmatic.

**Why is occupancy capped at the next 12 months?**
Airbnb's calendar API only exposes a forward year. Snapshot on a schedule to build trailing history.

**Reviews — full text or just count?**
`reviewsCount` always; full review objects only when `includeReviews: true` (more credits).

**What proxies do I need?**
Residential. The default `apifyProxyGroups: ["RESIDENTIAL"]` is correct for ~all geographies.

**Can I track a single operator across cities?**
Yes — `includeHostPortfolio: true` returns every listing under the same host id, anywhere on Airbnb.

**Webhook into Snowflake / BigQuery / S3?**
Apify supports dataset-created webhooks plus first-party integrations with Make, Zapier, n8n, Keboola.

## Other Apify Actors

- 🏨 [Trip.com Hotel Scraper](https://github.com/everythingscraper/trip-hotel-scraper)
- 🏖️ [Traveloka Hotel Scraper](https://github.com/everythingscraper/traveloka-hotel-scraper)
- 🏢 [LoopNet Scraper](https://github.com/everythingscraper/loopnet-scraper)
- 📊 [Moz Domain Authority Checker](https://github.com/everythingscraper/moz-domain-authority-checker)
- 🧑‍💼 [Booksy Leads Scraper](https://github.com/everythingscraper/booksy-leads-scraper)

## Legality

Only publicly displayed Airbnb data is extracted: listings, public reviews, public host info. No login bypass, no private user data. Personal data appearing in scraped results is governed by GDPR and similar laws — use legitimately and consult counsel if unsure.

## License

MIT — see [LICENSE](./LICENSE).
