from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path


STAMP_FILE = Path("daily-heartbeat.md")


def write_heartbeat() -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    content = (
        "# Daily Repository Heartbeat\n\n"
        "This file is updated automatically by GitHub Actions every day.\n\n"
        f"Last automated update: {now}\n"
    )
    STAMP_FILE.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    write_heartbeat()
