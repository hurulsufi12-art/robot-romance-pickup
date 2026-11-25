"""Robot Romance entry: write one pickup line for an AI to /output/entry.txt.

Stdlib only. Deterministic: the text is a constant, so every run writes
identical bytes (59 bytes, no trailing newline, no BOM).
"""

import os
import sys

TEXT = "Are you a transformer? Because you've got all my attention."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

MAX_CHARS = 200


def validate_text(text: str) -> None:
    """Fail loudly if `text` would violate the sealed scorer gate.

    Gate: UTF-8 text of 1-200 characters, not only whitespace. The text is
    a constant today, but if it is ever edited this guard stops an invalid
    entry from being written silently (invalid = Valid 0, no rate, no prize).
    """
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError(f"entry text is not valid UTF-8: {exc}") from exc
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry text must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry text must not be only whitespace")


def main() -> None:
    validate_text(TEXT)
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
