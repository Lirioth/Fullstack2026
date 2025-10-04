#!/usr/bin/env python3
"""Timed Challenge #1 — Reverse the Sentence (word-wise)

Reads a single line from standard input and prints the sentence reversed by words.

Example
Input : You have entered a wrong domain
Output: domain wrong a entered have You
"""

def reverse_words(line: str) -> str:
    # Split on any whitespace, reverse, join with single spaces
    words = line.split()
    words.reverse()
    return " ".join(words)

def main() -> None:
    try:
        line = input()
    except EOFError:
        line = ""
    print(reverse_words(line))

if __name__ == "__main__":
    main()
