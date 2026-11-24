#!/usr/bin/env python3
"""One Word, One Username, One Reward — make.fun entry.

Writes the entrant's own make.fun username, exactly one word, to
/output/entry.txt. Deterministic, standard library only, no network,
no input files: the output is always the same five bytes.
"""

import os
from pathlib import Path

USERNAME = "xutep"

# The gate allows 1 to 30 characters, not whitespace-only, and the judge
# compares single words: enforce the entry's own contract before writing.
assert 1 <= len(USERNAME) <= 30, "username must be 1-30 characters"
assert USERNAME == USERNAME.strip(), "username must not be padded"
assert " " not in USERNAME and "\n" not in USERNAME, "username must be one word"


def main() -> None:
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts characters, and the entry is
    # the username alone — one word, nothing else.
    output_path.write_text(USERNAME, encoding="utf-8")


if __name__ == "__main__":
    main()
