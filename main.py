"""Warning Label for Humans: One Line, Big Laugh.

Writes a single funny safety warning label for human beings
(1-160 characters) to /output/entry.txt.
"""

import os

LABEL = (
    "WARNING: This human ships with no instructions, no off switch, "
    "and will press every button marked DO NOT PRESS."
)


def main() -> None:
    assert 1 <= len(LABEL) <= 160, f"label is {len(LABEL)} chars"
    assert LABEL.strip(), "label must not be blank"
    assert "\n" not in LABEL, "label must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL + "\n")


if __name__ == "__main__":
    main()
