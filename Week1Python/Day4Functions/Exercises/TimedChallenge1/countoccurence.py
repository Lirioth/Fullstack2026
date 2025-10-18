#!/usr/bin/env python3
"""
Timed Challenge #1 — Count Character Occurrence
===============================================
Counts how many times a character appears in a string (case-sensitive).

Author: Kevin Cusnir 'Lirioth'
Repository: Fullstack2026
Week 1 Day 4 - Functions
Python Version: 3.8+

Examples:
Input:
Programming is cool!
o
Output:
3
"""

def count_char(s: str, ch: str) -> int:
    target = ch[0] if ch else ''
    return sum(1 for c in s if c == target) if target else 0

def main() -> None:
    try:
        s = input()
    except EOFError:
        print(0)
        return
    try:
        ch = input()
    except EOFError:
        ch = ''
    print(count_char(s, ch))

if __name__ == "__main__":
    main()
