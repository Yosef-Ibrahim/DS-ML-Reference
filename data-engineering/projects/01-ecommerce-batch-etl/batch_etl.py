"""
Credential-free e-commerce batch ETL reference implementation.

Author: Youssef Ibrahim Mohamed Soliman
GitHub: https://github.com/Yosef-Ibrahim
Email: youssefibrahimelisely@gmail.com
"""

from __future__ import annotations

import argparse
import csv
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

REQUIRED_COLUMNS = (
    "order_id",
    "customer_id",
    "order_ts",
    "product_id",
    "quantity",
    "unit_price",
    "currency",
)
DEFAULT_ROWS = (
    {
        "order_id": "O-1001",
        "customer_id": "C-001",
        "order_ts": "2026-01-02T09:15:00+00:00",
        "product_id": "P-100",
        "quantity": "2",
        "unit_price": "29.90",
        "currency": "USD",
    },
    {
        "order_id": "O-1002",
        "customer_id": "C-002",
        "order_ts": "2026-01-02T10:00:00+00:00",
        "product_id": "P-200",
        "quantity": "1",
        "unit_price": "75.00",
        "currency": "USD",
    },
    {
        "order_id": "O-1003",
        "customer_id": "C-001",
        "order_ts": "2026-01-03T12:30:00+00:00",
        "product_id": "P-100",
        "quantity": "3",
        "unit_price": "29.90",
        "currency": "USD",
    },
)


def parse_order(row: dict[str, str]) -> dict[str, object]:
    """Validate and normalize one CSV row, raising ValueError on bad data."""
    missing = [column for column in REQUIRED_COLUMNS if not row.get(column, "").strip()]
    if missing:
        raise ValueError(f"missing columns/values: {', '.join(missing)}")
    try:
        order_ts = datetime.fromisoformat(row["order_ts"].replace("Z", "+00:00"))
        quantity = int(row["quantity"])
        unit_price = float(row["unit_price"])
    except (TypeError, ValueError) as exc:
        raise ValueError(f"invalid timestamp, quantity, or unit_price: {exc}") from exc
    if order_ts.tzinfo is None:
        raise ValueError("order_ts must include a timezone")
    if quantity <= 0 or unit_price < 0:
        raise ValueError("quantity must be positive and unit_price non-negative")
    currency = row["currency"].strip().upper()
    if len(currency) != 3 or not currency.isalpha():
        raise ValueError("currency must be a three-letter code")
    return {
        "order_id": row["order_id"].strip(),
        "customer_id": row["customer_id"].strip(),
        "order_ts": order_ts.astimezone(timezone.utc).isoformat(),
        "product_id": row["product_id"].strip(),
        "quantity": quantity,
        "unit_price": unit_price,
        "currency": currency,
    }


def ensure_demo_input(path: Path) -> None:
    if path.exists():
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=REQUIRED_COLUMNS)
        writer.writeheader()
        writer.writerows(DEFAULT_ROWS)


def read_orders(path: Path) -> tuple[list[dict[str, object]], list[dict[str, str]]]:
    valid: list[dict[str, object]] = []
    rejected: list[dict[str, str]] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None or any(
            column not in reader.fieldnames for column in REQUIRED_COLUMNS
        ):
            raise ValueError(f"input must contain columns: {', '.join(REQUIRED_COLUMNS)}")
        for line_number, row in enumerate(reader, start=2):
            try:
                valid.append(parse_order(row))
            except ValueError as exc:
                rejected.append({"line": str(line_number), "reason": str(exc), **row})
    return valid, rejected


def load_orders(database: Path, orders: Iterable[dict[str, object]]) -> int:
    ddl = Path(__file__).with_name("schema_ddl.sql").read_text(encoding="utf-8")
    loaded_at = datetime.now(timezone.utc).isoformat()
    with sqlite3.connect(database) as connection:
        connection.executescript(ddl)
        count = 0
        for order in orders:
            connection.execute(
                "INSERT OR IGNORE INTO customers(customer_id, first_seen_at) VALUES (?, ?)",
                (order["customer_id"], order["order_ts"]),
            )
            connection.execute(
                "INSERT OR IGNORE INTO products(product_id, product_name, category) "
                "VALUES (?, ?, ?)",
                (order["product_id"], f"Product {order['product_id']}", "unknown"),
            )
            cursor = connection.execute(
                """
                INSERT OR REPLACE INTO orders
                (order_id, customer_id, product_id, order_ts, quantity,
                 unit_price, currency, loaded_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    order["order_id"],
                    order["customer_id"],
                    order["product_id"],
                    order["order_ts"],
                    order["quantity"],
                    order["unit_price"],
                    order["currency"],
                    loaded_at,
                ),
            )
            count += cursor.rowcount
        connection.commit()
    return count


def write_rejects(path: Path, rows: list[dict[str, str]]) -> None:
    if not rows:
        path.unlink(missing_ok=True)
        return
    fields = ["line", "reason", *REQUIRED_COLUMNS]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("orders.csv"))
    parser.add_argument("--database", type=Path, default=Path("ecommerce.db"))
    parser.add_argument("--rejects", type=Path, default=Path("rejects.csv"))
    parser.add_argument("--demo", action="store_true", help="create the sample input if absent")
    args = parser.parse_args()
    if args.demo:
        ensure_demo_input(args.input)
    if not args.input.exists():
        raise FileNotFoundError(f"input file does not exist: {args.input}")
    valid, rejected = read_orders(args.input)
    loaded = load_orders(args.database, valid)
    write_rejects(args.rejects, rejected)
    print(f"Loaded {loaded} order(s); rejected {len(rejected)} row(s).")
    print(f"SQLite database: {args.database}")


if __name__ == "__main__":
    main()
