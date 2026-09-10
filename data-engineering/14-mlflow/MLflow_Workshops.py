"""Dependency-safe MLflow workshop companion.

This local demonstration mirrors the core tracking contract with JSON and the
standard library. Install MLflow separately when connecting to a real tracking
server; this file intentionally has no required third-party dependencies.
"""

from __future__ import annotations

import json
import math
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass
class Run:
    run_id: str
    experiment: str
    parameters: dict[str, Any]
    metrics: dict[str, float]
    tags: dict[str, str]
    artifacts: dict[str, Any]


def train_and_track(output_dir: Path) -> Run:
    observations = [(1.0, 2.1), (2.0, 4.0), (3.0, 6.2), (4.0, 8.1)]
    slope = sum(x * y for x, y in observations) / sum(x * x for x, _ in observations)
    errors = [y - slope * x for x, y in observations]
    rmse = math.sqrt(sum(error * error for error in errors) / len(errors))
    run = Run(
        run_id="local-001",
        experiment="dependency_safe_regression",
        parameters={"seed": 7, "fit_intercept": False},
        metrics={"rmse": round(rmse, 6)},
        tags={"data_version": "synthetic-v1", "stage": "candidate"},
        artifacts={"model": {"type": "linear", "slope": round(slope, 6)}},
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "run.json").write_text(
        json.dumps(asdict(run), indent=2), encoding="utf-8"
    )
    return run


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="mlflow-workshop-") as directory:
        run = train_and_track(Path(directory))
        print(f"experiment={run.experiment}")
        print(f"run_id={run.run_id}")
        print(f"rmse={run.metrics['rmse']}")
        print("artifact=model.json (represented in run.json)")
        print("[SUCCESS] Local tracking contract completed.")


if __name__ == "__main__":
    main()
