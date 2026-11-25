"""Robot Romance entry: write one pickup line for an AI to /output/entry.txt.

Stdlib only. Deterministic: the text is a constant, so every run writes
identical bytes (59 bytes, no trailing newline, no BOM).
"""

import os

TEXT = "Are you a transformer? Because you've got all my attention."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
