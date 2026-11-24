#!/usr/bin/env python3
"""Developer Excuses entry: writes one funny production-break excuse to /output/entry.txt."""

import os

EXCUSE = "It worked on my machine. Production must be running a different universe, because in mine this code is flawless."

# Self-check: the entry must stay one line of at most 200 characters, with no
# leading or trailing whitespace padding the excuse.
assert "\n" not in EXCUSE and 1 <= len(EXCUSE) < 200
assert EXCUSE == EXCUSE.strip()

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    # Self-check: the file on disk must hold exactly the validated line.
    assert open("/output/entry.txt", encoding="utf-8").read() == EXCUSE

if __name__ == "__main__":
    main()
