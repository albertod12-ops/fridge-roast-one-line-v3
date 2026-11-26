"""Fridge Roast v3: a single-line roast of a smart fridge.

Writes the line to entry.txt under MAKEFUN_OUTPUT_DIR (or /output),
mode 0644, no trailing newline. Standard library only. The line is a
constant, so every run produces byte-identical output.
"""

from pathlib import Path
import os

LINE_JOKE = (
    "My smart fridge called my oat milk 'a cry for help', recommended "
    "whole milk instead, then expired it two days early just to win "
    "the argument."
)


def assemble() -> str:
    joke = LINE_JOKE
    if len(joke) > 200 or not joke.strip():
        raise ValueError("roast line must be 1-200 non-blank characters")
    if joke != joke.strip():
        raise ValueError("roast line must not start or end with whitespace")
    return joke


def emit_line() -> Path:
    os.umask(0o022)
    dest_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "entry.txt"
    dest.write_text(assemble(), encoding="utf-8", newline="")
    dest.chmod(0o644)
    return dest


if __name__ == "__main__":
    emit_line()
