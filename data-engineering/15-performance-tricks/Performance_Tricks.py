"""Dependency-safe performance workshop companion using only the standard library."""

from __future__ import annotations

import sqlite3
import time


def benchmark_query(row_count: int = 20_000) -> tuple[float, float]:
    connection = sqlite3.connect(":memory:")
    connection.execute("CREATE TABLE events (event_id INTEGER PRIMARY KEY, region TEXT, amount REAL)")
    connection.executemany(
        "INSERT INTO events VALUES (?, ?, ?)",
        ((index, f"region-{index % 10}", float(index % 100)) for index in range(row_count)),
    )
    connection.commit()

    start = time.perf_counter()
    total = connection.execute(
        "SELECT region, SUM(amount) FROM events WHERE event_id >= ? GROUP BY region",
        (row_count // 2,),
    ).fetchall()
    elapsed = time.perf_counter() - start
    connection.close()
    return elapsed, sum(amount for _, amount in total)


def main() -> None:
    elapsed, total = benchmark_query()
    print(f"filtered_grouped_total={total:.2f}")
    print(f"elapsed_seconds={elapsed:.6f}")
    print("Measure first; then compare one change at a time with the same workload.")


if __name__ == "__main__":
    main()
