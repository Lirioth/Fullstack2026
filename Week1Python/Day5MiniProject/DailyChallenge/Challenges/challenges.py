s = input("Enter comma-separated words: ")
import re
from typing import List


# Challenge 1: Sorting 🧩
def sort_comma_separated(words: str) -> List[str]:
    """Return sorted words extracted from a comma-separated string."""

    cleaned = [part.strip() for part in words.split(",") if part.strip()]
    return sorted(cleaned)


# Challenge 2: Longest Word 🧠
def longest_word(sentence: str) -> str:
    words = sentence.split()
    best = ""
    longest_length = 0
    for w in words:
        cleaned = re.sub(r"[^A-Za-z]", "", w)
        if not cleaned:
            continue
        if len(cleaned) > longest_length:
            best = w
            longest_length = len(cleaned)
    return best


def _cli() -> None:
    """Run the original interactive prompts."""

    entries = sort_comma_separated(input("Enter comma-separated words: "))
    if entries:
        print(",".join(entries))
    else:
        print("No valid words were provided 🤖")


if __name__ == "__main__":
    _cli()
    # Quick sanity checks 🤖
    assert longest_word("Margaret's toy is a pretty doll.") == "Margaret's"
    assert longest_word("A thing of beauty is a joy forever.") == "forever."
    assert longest_word("Forgetfulness is by all means powerless!") == "Forgetfulness"
    assert longest_word("Wow!!! So??? yes.") == "Wow!!!"
    assert longest_word("!!! 123 ...") == ""
