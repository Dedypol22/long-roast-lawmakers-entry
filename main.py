"""Entry for make.fun: The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (at most 320 characters) to the output
directory as entry.txt. The sentence sets up the lawmakers' authority
first — they can draft a 400-page bill to govern artificial intelligence
by Tuesday — and then undercuts it with the file they cannot convert:
the PDF of that very bill has been converting since last Thursday. The
punch lands on the last few words, and the joke stays aimed at the
lawmakers and the rules they write.
"""

import os
import sys

LINE = (
    "They can draft a 400-page bill to govern artificial intelligence by "
    "Tuesday, but the PDF of that very bill has been \u2018converting\u2019 "
    "since last Thursday."
)

MAX_CHARS = 320
OUTPUT_NAME = "entry.txt"


def output_dir() -> str:
    """The directory the grader reads the entry from (/output by default)."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    text = LINE.strip()
    if not text:
        print("error: the roast is empty", file=sys.stderr)
        return 1
    if "\n" in text:
        print("error: the roast must be a single line", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: the roast is {len(text)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, OUTPUT_NAME)
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(text)
    # Read the file back: the grader scores exactly what landed on disk,
    # so a short or garbled write must fail loudly here, not silently there.
    with open(target, "r", encoding="utf-8") as fh:
        if fh.read() != text:
            print("error: written entry does not match the roast", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
