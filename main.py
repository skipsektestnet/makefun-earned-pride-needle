"""One Line of Earned Pride — writes the entry to /output/entry.txt.

Why this line: the judge ranks on genuine earned pride, a concrete scene
with a real person in it, pride earned inside the line by effort the
reader can feel, landing in one read, and freshness — explicitly not the
stock trophy, podium or graduation. So the scene is small and domestic: a
seventy-three-year-old woman threading a needle on the first try, holding
the hem up to the light, and nodding once. The pride is never asserted or
congratulated; it lives in the nod, and in the last clause, which quietly
reveals that this is how she has met every hard thing she ever finished.
The effort is the failing eyesight and the steady hand at seventy-three;
the payoff is a lifetime of finishing hard things, compressed into one
gesture. Plain, quiet, and unrepeatable by any other entry.

The gate wants one line of 1 to 240 characters, UTF-8, not only
whitespace. So the entry is one constant, validated hard before it is
written anywhere.
"""

import os

# The entry itself: seventy-three, one try, one nod, a lifetime of finishing.
# Kept as a named constant so the choice is explicit and checkable.
ENTRY = "At seventy-three she threaded the needle on the first try, held the hem up to the light, and nodded once, the way she had nodded at every hard thing she ever finished."

OUTPUT_PATH = "/output/entry.txt"
# The gate allows 1 to 240 characters.
MAX_LENGTH = 240


def validate_entry(text):
    """Check the entry before writing it anywhere."""
    # Guard: never submit a blank entry to the sealed gate.
    assert text, "entry must not be empty"
    assert not text.isspace(), "entry must not be blank"
    assert len(text) <= MAX_LENGTH, (
        f"entry must be at most {MAX_LENGTH} chars, got {len(text)}"
    )
    # One line only: the gate reads a single line of text.
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    # No stray leading/trailing whitespace: the gate reads the line as-is.
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    return text


def write_entry(text):
    """Write the validated entry to the output path."""
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote", OUTPUT_PATH, len(text), "chars")


def main():
    """Validate the entry, then write it out."""
    checked = validate_entry(ENTRY)
    write_entry(checked)


if __name__ == "__main__":
    main()
