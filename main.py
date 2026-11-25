#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph — entry writer.

Writes exactly one line to /output/entry.txt: a tombstone epitaph.

Why this line: it opens in a true epitaph voice ("Here lies Tom"), borrows
a boast everyone has heard — "I'll sleep when I'm dead" — and then lets
the stone itself deliver the verdict in three words: he was right. The
joke needs no setup beyond the cliché, the twist is the dead man being
proved right by his own tombstone, and the whole thing reads like
something actually carved — short, final, and easy to repeat to a friend.
"""

import os

ENTRY = "Here lies Tom. He always said he'd sleep when he was dead. He was right."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(ENTRY) <= 150, "entry must be 1-150 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
