"""The Internet in One Word: a single word for the whole internet.

Writes one word to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure standard library; runs under `python3 -P -s` in the grader sandbox.
"""

import os

LINE = "doomscroll"


def main():
    # The gate wants one word: 1 to 30 characters, no white space at all.
    if not (1 <= len(LINE) <= 30 and LINE.split() == [LINE]):
        raise ValueError("entry is not a single word inside the 1-30 character gate")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the entry is the word, exactly as written.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
