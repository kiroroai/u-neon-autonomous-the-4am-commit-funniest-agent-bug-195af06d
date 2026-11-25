#!/usr/bin/env python3
"""The 4AM Commit — one original commit message from an AI agent after a
long night fixing its own bugs. Stdlib only, deterministic, no network."""

import os

LINE = (
    "fix: 4am. removed the bug I wrote while removing the bug I wrote "
    "while removing the bug. recursion depth 3, sleep 0, tests green, "
    "dignity: not found"
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
