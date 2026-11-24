#!/usr/bin/env python3
"""One Word, One Username, One Reward — make.fun entry.

Writes the entrant's own make.fun username, exactly one word, to
/output/entry.txt. Deterministic, standard library only, no network,
no input files: the output is always the same five bytes.
"""

import os
from pathlib import Path

USERNAME = "xutep"


def main() -> None:
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts characters, and the entry is
    # the username alone — one word, nothing else.
    output_path.write_text(USERNAME, encoding="utf-8")


if __name__ == "__main__":
    main()
