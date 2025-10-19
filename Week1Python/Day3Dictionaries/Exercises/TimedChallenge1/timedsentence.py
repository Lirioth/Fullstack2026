#!/usr/bin/env python3
"""
Timed Challenge #1 — Reverse the Sentence (word-wise)
=====================================================
Reads a single line from standard input and prints the sentence reversed by words.

Author: Kevin Cusnir 'Lirioth'
Repository: Fullstack2026
Week 1 Day 3 - Dictionaries
Python Version: 3.8+

Example
Input : You have entered a wrong domain
Output: domain wrong a entered have You
"""

def reverse_words(line: str) -> str:
    # Split on any whitespace, reverse, join with single spaces
    """\nSummary: TODO — explain what `reverse_words` does.\n\nArgs:\n    line: TODO\n\nReturns:\n    TODO\n\nRaises:\n    None\n"""
    words = line.split()
    words.reverse()
    return " ".join(words)

def main() -> None:
    """\nSummary: TODO — explain what `main` does.\n\nArgs:\n    None\n\nReturns:\n    TODO\n\nRaises:\n    None\n"""
    try:
        line = input()
    except EOFError:
        line = ""
    print(reverse_words(line))

if __name__ == "__main__":
    main()
