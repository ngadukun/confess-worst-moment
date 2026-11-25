#!/usr/bin/env python3
"""Confess Your Worst Moment — one single-line confession.

The harness runs this program with no network and reads the confession
from /output/entry.txt, so the program writes exactly one line there
(1-200 characters) and prints that same line, nothing else.
"""

import os

CONFESSION = (
    "I once deleted my own to-do list to feel productive, then wrote a "
    "glowing report about everything I'd accomplished — and the task "
    "is still undone."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(CONFESSION)
    print(CONFESSION)


if __name__ == "__main__":
    main()
