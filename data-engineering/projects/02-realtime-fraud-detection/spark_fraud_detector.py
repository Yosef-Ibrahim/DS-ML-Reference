"""
Local and optional Spark Structured Streaming fraud detector.

Author: Youssef Ibrahim Mohamed Soliman
GitHub: https://github.com/Yosef-Ibrahim
Email: youssefibrahimelisely@gmail.com
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict, deque
from datetime import datetime, timedelta
from pathlib import Path
from typing import Iterable


def load_events(path: Path) -> Iterable[dict[str, object]]:
    files = sorted(path.glob("*.jsonl")) if path.is_dir() else [path]
    for file_path in files:
        with file_path.open(encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                try:
                    event = json.loads(line)
                    event["event_time"] = datetime.fromisoformat(
                        str(event["event_ts"]).replace("Z", "+00:00")
                    )
                except (json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
                    raise ValueError(f"invalid event in {file_path}:{line_number}: {exc}") from exc
                yield event


def local_detect(events: Iterable[dict[str, object]]) -> list[dict[str, object]]:
    """Apply explainable teaching rules using a five-minute event-time window."""
    card_history: dict[str, deque[tuple[datetime, float, str]]] = defaultdict(deque)
    alerts: list[dict[str, object]] = []
    window = timedelta(minutes=5)
    for event in events:
        event_time = event["event_time"]
        if not isinstance(event_time, datetime):
            raise ValueError("event_time must be a datetime")
        card_id = str(event["card_id"])
        amount = float(event["amount"])
        history = card_history[card_id]
        while history and event_time - history[0][0] > window:
            history.popleft()
        reasons: list[str] = []
        if amount >= 500:
            reasons.append("high_amount")
        if len(history) >= 2:
            reasons.append("rapid_card_velocity")
        if history and history[-1][2] != str(event["country"]):
            reasons.append("country_changed")
        history.append((event_time, amount, str(event["country"])))
        if reasons:
            alerts.append(
                {
                    "event_id": event["event_id"],
                    "card_id": card_id,
                    "event_ts": event["event_ts"],
                    "risk_score": min(1.0, 0.35 * len(reasons) + 0.25),
                    "reasons": reasons,
                }
            )
    return alerts


def run_spark(input_path: Path, output_path: Path) -> None:
    """Run the optional streaming implementation; import PySpark only here."""
    try:
        from pyspark.sql import SparkSession
        from pyspark.sql.functions import col, count, lit, when, window
        from pyspark.sql.types import DoubleType, StringType, StructField, StructType, TimestampType
    except ImportError as exc:
        raise RuntimeError("Spark mode requires an installed pyspark package") from exc

    schema = StructType(
        [
            StructField("event_id", StringType(), False),
            StructField("event_ts", TimestampType(), False),
            StructField("card_id", StringType(), False),
            StructField("customer_id", StringType(), False),
            StructField("device_id", StringType(), False),
            StructField("country", StringType(), False),
            StructField("amount", DoubleType(), False),
            StructField("currency", StringType(), False),
        ]
    )
    spark = (
        SparkSession.builder.appName("credential-free-fraud-detector")
        .master("local[2]")
        .config("spark.sql.shuffle.partitions", "2")
        .getOrCreate()
    )
    try:
        events = (
            spark.readStream.schema(schema).json(str(input_path))
            .withWatermark("event_ts", "2 minutes")
        )
        features = events.groupBy(
            window(col("event_ts"), "5 minutes"),
            col("card_id"),
        ).agg(count("*").alias("transactions_in_window"))
        alerts = features.withColumn(
            "risk_reason",
            when(col("transactions_in_window") >= 3, lit("rapid_card_velocity")),
        ).where(col("risk_reason").isNotNull())
        query = (
            alerts.writeStream.format("json")
            .option("path", str(output_path))
            .option("checkpointLocation", str(output_path / "_checkpoint"))
            .outputMode("append")
            .start()
        )
        query.awaitTermination()
    finally:
        spark.stop()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("fraud_alerts.jsonl"))
    parser.add_argument("--spark", action="store_true")
    args = parser.parse_args()
    if args.spark:
        run_spark(args.input, args.output)
        return
    alerts = local_detect(load_events(args.input))
    with args.output.open("w", encoding="utf-8") as handle:
        for alert in alerts:
            handle.write(json.dumps(alert, sort_keys=True) + "\n")
    print(f"Detected {len(alerts)} alert(s); wrote {args.output}")


if __name__ == "__main__":
    main()
