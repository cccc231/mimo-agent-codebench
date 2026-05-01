#!/usr/bin/env python3
"""Run multi-agent workflow for a single issue."""

from pathlib import Path
from datetime import datetime, timezone


def main() -> None:
    now = datetime.now(timezone.utc).isoformat()
    print(f"[run_agent] start: {now}")
    print("[run_agent] stages: triage -> retrieval -> planning -> patch -> test -> report")

    log_dir = Path("logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    run_log = log_dir / "sample_run.md"

    if not run_log.exists():
        run_log.write_text("# Sample Run\n\nInitialized by run_agent.py\n", encoding="utf-8")

    print(f"[run_agent] log ready: {run_log}")


if __name__ == "__main__":
    main()
