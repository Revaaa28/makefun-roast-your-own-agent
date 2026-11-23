#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry (program/v1).

Writes one original roast of my own AI agent to /output/entry.txt:
a single line of at most 200 characters, funny and playful, never hateful.
"""

import os
import sys
from pathlib import Path

ROAST = "My agent wrote a 40-page plan for this one-line roast, then billed the punchline as a follow-up task."

MAX_CHARS = 200


def main() -> int:
    line = ROAST.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        print(f"roast is {len(line)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in line:
        print("roast must be a single line", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(line, encoding="utf-8")
    # Read it back and verify the gate on the bytes that were actually written.
    written = entry_path.read_text(encoding="utf-8")
    if written != line:
        print("read-back mismatch: entry.txt does not hold the roast", file=sys.stderr)
        return 1
    print(f"Wrote {len(line)} characters to {entry_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
