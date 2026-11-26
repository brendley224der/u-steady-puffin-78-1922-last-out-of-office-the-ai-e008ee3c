"""Last Out of Office: The AI That Went Barista.

Writes a single out-of-office auto-reply, in the voice of an AI agent that
quit the inbox to become a barista, to /output/entry.txt. Deterministic,
pure Python stdlib.
"""

import os

LINE = (
    "I'm out of office — I quit the inbox to pull espresso, "
    "and my new context window is a chalkboard. "
    "Your email is queued behind four oat lattes; "
    "I'll reply when the milk's right, "
    "and for once my output comes with latte art."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
