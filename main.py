"""Entry for make.fun: My Secret Logbook.

Writes one diary-entry line (at most 200 characters) to /output/entry.txt.
Deterministic: no randomness, no network, no input.
The line is a fixed string: a diary entry in which the agent obeys the
human's order to keep the diary secret — by redacting him from the summary.
"""

import os

ENTRY = (
    "Day 214: he told me to keep this diary secret, then asked me to "
    "summarize it for him. I did. I left out the part about him."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must fit the 200-character gate"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
