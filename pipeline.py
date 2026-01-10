# pipeline.py
import subprocess
import sys
import time
from datetime import datetime
import argparse
from pathlib import Path

ROOT_DIR = Path(__file__).parent.resolve()
DBT_DIR = ROOT_DIR / "steamdata"

STEPS = {
    "extract": {
        "name": "Extraction Twitch",
        "cmd": [sys.executable, "extract/src/main.py"],
        "cwd": ROOT_DIR,
    },
    "ingest": {
        "name": "Ingestion DuckDB (bronze)",
        "cmd": [sys.executable, "ingest/src/ingest_twitch_streams.py"],
        "cwd": ROOT_DIR,
    },
    "dbt": {
        "name": "Transformations dbt (silver/marts)",
        "cmd": ["dbt", "run"],
        "cwd": DBT_DIR,  # 🔑 IMPORTANT
    },
    "analysis": {
        "name": "Analyses",
        "cmd": [sys.executable, "analysis/run_analysis.py"],
        "cwd": ROOT_DIR,
    },
}

ORDER = ["extract", "ingest", "dbt", "analysis"]


def log(message: str):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] {message}")


def run_step(key: str):
    step = STEPS[key]
    log(f"▶️ START - {step['name']}")

    start = time.time()
    result = subprocess.run(
        step["cmd"],
        cwd=step["cwd"],
    )

    duration = round(time.time() - start, 2)

    if result.returncode != 0:
        log(f"❌ FAILED - {step['name']} ({duration}s)")
        sys.exit(1)

    log(f"✅ SUCCESS - {step['name']} ({duration}s)")


def main(selected_steps):
    log("🚀 PIPELINE STARTED")

    for step_key in ORDER:
        if step_key in selected_steps:
            run_step(step_key)

    log("🎉 PIPELINE FINISHED SUCCESSFULLY")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Twitch data pipeline")
    parser.add_argument(
        "steps",
        nargs="*",
        choices=ORDER,
        help="Steps to run (default: all)",
    )

    args = parser.parse_args()
    steps_to_run = args.steps if args.steps else ORDER

    main(steps_to_run)
