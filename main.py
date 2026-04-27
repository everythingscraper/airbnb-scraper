"""Airbnb Full-Data Scraper — Apify Actor client example.

Runs the Actor for a single search, writes the dataset to airbnb_results.json,
and prints aggregate STR metrics (mean occupancy / ADR / RevPAR).

Docs: https://apify.com/hotels-scrapers/airbnb-scraper
"""

import json
import os
import statistics
from pathlib import Path

from apify_client import ApifyClient

ACTOR = "hotels-scrapers/airbnb-scraper"
OUTPUT_FILE = Path("airbnb_results.json")


def _mean(values: list[float]) -> float:
    return statistics.mean(values) if values else 0.0


def main() -> None:
    token = os.environ.get("APIFY_TOKEN") or _die("Set APIFY_TOKEN — https://console.apify.com/settings/integrations")
    client = ApifyClient(token)

    run_input = {
        "mode": "search",
        "location": "Paris, France",
        "checkIn": "2026-06-01",
        "checkOut": "2026-06-07",
        "maxListings": 10,
        "currency": "EUR",
        "proxyConfiguration": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"]},
    }

    print(f"[airbnb] starting actor {ACTOR}")
    run = client.actor(ACTOR).call(run_input=run_input)
    print(f"[airbnb] {run['status']}  •  run_id={run['id']}")

    items = client.dataset(run["defaultDatasetId"]).list_items().items
    OUTPUT_FILE.write_text(json.dumps(items, indent=2, ensure_ascii=False))
    print(f"[airbnb] saved {len(items)} listings → {OUTPUT_FILE}\n")

    occ = [i["occupancyRate"] for i in items if i.get("occupancyRate") is not None]
    adr = [i["ADR"] for i in items if i.get("ADR") is not None]
    rev = [i["RevPAR"] for i in items if i.get("RevPAR") is not None]

    print("market summary")
    print(f"  listings analysed : {len(items)}")
    print(f"  mean occupancy    : {_mean(occ):.1%}")
    print(f"  mean ADR          : {_mean(adr):.2f}")
    print(f"  mean RevPAR       : {_mean(rev):.2f}")
    print(f"\nconsole → https://console.apify.com/actors/runs/{run['id']}")


def _die(msg: str) -> str:
    raise SystemExit(msg)


if __name__ == "__main__":
    main()
