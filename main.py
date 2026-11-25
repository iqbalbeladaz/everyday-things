#!/usr/bin/env python3
"""Everyday Things, Two Lines — entry program.

Writes the two-line explanation to /output/entry.txt.
Deterministic: the same bytes on every run, no input, no randomness.

Line 1 explains one everyday thing — a queue — to a 10-year-old in a single
vivid sentence built on one analogy: a caterpillar made of people.
Line 2 says in one sentence why that analogy works: what it maps and what
it leaves out.
"""

from pathlib import Path

ENTRY = (
    "A queue is a caterpillar made of people, shuffling forward one tiny step at a time whenever its head moves.\n"
    "It maps how the whole line moves from the front, one step at a time, but leaves out that, unlike a real caterpillar, nobody is attached and anyone can leave, join, or pick another line.\n"
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
