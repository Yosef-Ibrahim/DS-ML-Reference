"""
Local-first bronze/silver/gold lakehouse ETL.

Author: Youssef Ibrahim Mohamed Soliman
GitHub: https://github.com/Yosef-Ibrahim
Email: youssefibrahimelisely@gmail.com
"""

from __future__ import annotations

import argparse
import json
import shutil
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SAMPLE_EVENTS = (
    {"event_id": "e-001", "event_ts": "2026-01-02T09:00:00+00:00", "customer_id": "c-1", "amount": 20.0},
    {"event_id": "e-002", "event_ts": "2026-01-02T10:00:00+00:00", "customer_id": "c-2", "amount": 35.5},
    {"event_id": "e-003", "event_ts": "2026-01-03T11:00:00+00:00", "customer_id": "c-1", "amount": 12.0},
)


def ensure_sample(path: Path) -> None:
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for event in SAMPLE_EVENTS:
            handle.write(json.dumps(event, sort_keys=True) + "\n")


def read_events(path: Path) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
            event["event_ts"] = datetime.fromisoformat(
                str(event["event_ts"]).replace("Z", "+00:00")
            ).astimezone(timezone.utc).isoformat()
            event["amount"] = float(event["amount"])
            if not event["event_id"] or not event["customer_id"] or event["amount"] < 0:
                raise ValueError("missing ID or negative amount")
        except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
            raise ValueError(f"invalid event at {path}:{line_number}: {exc}") from exc
        events.append(event)
    return events


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True) + "\n")


def run_pipeline(input_path: Path, root: Path) -> dict[str, int]:
    events = read_events(input_path)
    bronze = root / "bronze" / input_path.name
    silver = root / "silver" / "events.jsonl"
    gold = root / "gold" / "daily_revenue.jsonl"
    root.mkdir(parents=True, exist_ok=True)
    bronze.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(input_path, bronze)

    unique_events = {str(event["event_id"]): event for event in events}
    silver_rows = sorted(unique_events.values(), key=lambda event: str(event["event_ts"]))
    write_jsonl(silver, silver_rows)

    totals: dict[tuple[str, str], dict[str, Any]] = defaultdict(
        lambda: {"event_date": "", "customer_id": "", "event_count": 0, "revenue": 0.0}
    )
    for event in silver_rows:
        key = (str(event["event_ts"])[:10], str(event["customer_id"]))
        row = totals[key]
        row["event_date"], row["customer_id"] = key
        row["event_count"] += 1
        row["revenue"] = round(float(row["revenue"]) + float(event["amount"]), 2)
    gold_rows = sorted(totals.values(), key=lambda row: (row["event_date"], row["customer_id"]))
    write_jsonl(gold, gold_rows)

    manifest = {
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "source": str(input_path),
        "bronze_rows": len(events),
        "silver_rows": len(silver_rows),
        "gold_rows": len(gold_rows),
    }
    (root / "run_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return {key: value for key, value in manifest.items() if key.endswith("_rows")}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("sample_events.jsonl"))
    parser.add_argument("--root", type=Path, default=Path("lakehouse"))
    args = parser.parse_args()
    ensure_sample(args.input)
    counts = run_pipeline(args.input, args.root)
    print("Medallion pipeline complete: " + ", ".join(f"{key}={value}" for key, value in counts.items()))


if __name__ == "__main__":
    main()
