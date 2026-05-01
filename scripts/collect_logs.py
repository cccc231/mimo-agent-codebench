#!/usr/bin/env python3
"""Collect and summarize workflow logs."""

from pathlib import Path


def main() -> None:
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    logs = sorted(log_dir.glob("*.md"))
    print(f"[collect_logs] found {len(logs)} markdown logs")
    for log in logs:
        print(f" - {log}")


if __name__ == "__main__":
    main()
