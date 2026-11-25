import os
from pathlib import Path

FINAL_EMOJI = "🐙"


def emit(emoji: str) -> None:
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_text(emoji, encoding="utf-8")


if __name__ == "__main__":
    emit(FINAL_EMOJI)
