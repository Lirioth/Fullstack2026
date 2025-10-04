"""Daily challenge: Build up a string."""

from __future__ import annotations

import random


def validate_length(text: str) -> tuple[bool, str]:
    """Return whether the text is exactly 10 characters with a feedback message."""
    if len(text) < 10:
        return False, "String not long enough."
    if len(text) > 10:
        return False, "String too long."
    return True, "Perfect string"


def build_up_text(text: str) -> None:
    """Print the incremental build-up of the provided text."""
    built = ""
    for ch in text:
        built += ch
        print(built)


def jumble_text(text: str) -> str:
    """Return a shuffled version of the provided text."""
    chars = list(text)
    random.shuffle(chars)
    return "".join(chars)


def main() -> None:
    """Run the interactive build-up challenge."""
    user_input = input("Enter a string (must be exactly 10 characters): ")
    is_valid, message = validate_length(user_input)
    print(message)
    if not is_valid:
        return

    # 🧩 Show the first and last characters for quick insights.
    print("First character:", user_input[0])
    print("Last character:", user_input[-1])

    # 🚧 Build the string character by character for visualization.
    build_up_text(user_input)

    # 🔀 Display a jumbled version for fun.
    print("Jumbled string:", jumble_text(user_input))


if __name__ == "__main__":
    main()
