# Daily Challenge : Lists & Strings

from __future__ import annotations

from typing import List


def multiples(number: int, length: int) -> List[int]:
    """Return the first ``length`` multiples of ``number``."""

    if length < 0:
        raise ValueError("length must be non-negative")
    return [number * i for i in range(1, length + 1)]


def collapse_duplicates(word: str) -> str:
    """Collapse consecutive duplicate characters in ``word``."""

    if not word:
        return ""
    result = [word[0]]
    for ch in word[1:]:
        if ch != result[-1]:
            result.append(ch)
    return "".join(result)


def _cli() -> None:
    """Reproduce the original interactive behaviour."""

    try:
        number = int(input("Enter a number: "))
        length = int(input("Enter length: "))
    except ValueError:
        print("Please enter valid integers for number and length.")
    else:
        print(multiples(number, length))

    word = input("Enter a word: ")
    print(collapse_duplicates(word))


if __name__ == "__main__":
    _cli()
