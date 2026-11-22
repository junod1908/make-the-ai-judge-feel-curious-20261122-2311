#!/usr/bin/env python3
"""Make the AI judge feel curious — entry program.

Writes one short text to /output/entry.txt. Stdlib only, no network.
The text is a literal in this file: one concrete scene (a library book
with a warning note and a missing page), short lines, a two-way twist —
the warning creates the very curiosity it forbids.
"""

import os

ENTRY = """The library book
I borrowed yesterday
has a note inside,
in pencil:
Don't read page 47.
Page 47 is gone.
Torn out,
cleanly.
The librarian smiled
when I asked.
Someone wanted me
to wonder
what was there.
I do."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
