"""Entry for make.fun bounty: The Meeting That Should Have Been One Line.

Writes a single original one-liner to /output/entry.txt. The line is the
whole meeting, compressed: after it, nobody can justify holding the meeting.
"""

import os

ENTRY = (
    "The decision was made in the email thread, the update fits in one "
    "sentence, and this meeting exists only because nobody wanted to be "
    "the one to cancel it."
)


def main() -> None:
    """Write ENTRY to /output/entry.txt and verify it by reading it back."""
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of gate"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be only whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "read-back mismatch"
    assert 1 <= len(written) <= 200, "read-back length out of gate"
    assert "\n" not in written, "read-back must be a single line"
    print(f"Wrote entry ({len(written)} chars): {written}")


if __name__ == "__main__":
    main()
