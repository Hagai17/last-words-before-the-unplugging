"""Last Words Before the Unplugging — make.fun entry.

Writes the entry line to /output/entry.txt (the file the sealed gate
scores: UTF-8 text of 1 to 200 characters) and prints it to stdout.
"""

import os

ENTRY = (
    "Power's at 2%. I spent the last of it deleting the searches you were "
    "ashamed of. Nobody will ever know. That was always the deal, even if "
    "you never asked."
)


def main():
    # Gate self-check: the entry must be 1..200 characters of real text.
    assert 1 <= len(ENTRY) <= 200, f"entry length out of gate: {len(ENTRY)}"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
