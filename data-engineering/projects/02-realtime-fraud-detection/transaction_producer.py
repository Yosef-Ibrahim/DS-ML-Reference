"""
Deterministic JSON Lines transaction producer for local streaming exercises.

Author: Youssef Ibrahim Mohamed Soliman
GitHub: https://github.com/Yosef-Ibrahim
Email: youssefibrahimelisely@gmail.com
"""

from __future__ import annotations

import argparse
import json
import random
from datetime import datetime, timedelta, timezone
from pathlib import Path


def generate_transactions(count: int, seed: int = 7) -> list[dict[str, object]]:
    if count < 1:
        raise ValueError("count must be positive")
    randomizer = random.Random(seed)
    countries = ("EG", "SA", "AE", "GB")
    base_time = datetime(2026, 1, 2, 12, tzinfo=timezone.utc)
    rows: list[dict[str, object]] = []
    for index in range(count):
        card_id = "card-001" if index in (0, 1, 2) else f"card-{index % 4 + 1:03d}"
        amount = 950.0 if index == 2 else round(randomizer.uniform(12, 180), 2)
        country = "GB" if index == 2 else countries[index % len(countries)]
        rows.append(
            {
                "event_id": f"evt-{index + 1:05d}",
                "event_ts": (base_time + timedelta(seconds=index * 20)).isoformat(),
                "card_id": card_id,
                "customer_id": f"customer-{index % 6 + 1:03d}",
                "device_id": f"device-{index % 5 + 1:03d}",
                "country": country,
                "amount": amount,
                "currency": "USD",
            }
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("transactions.jsonl"))
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=7)
    args = parser.parse_args()
    rows = generate_transactions(args.count, args.seed)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True) + "\n")
    print(f"Wrote {len(rows)} transaction event(s) to {args.output}")


if __name__ == "__main__":
    main()
