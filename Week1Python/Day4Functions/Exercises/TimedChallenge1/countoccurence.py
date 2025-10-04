#!/usr/bin/env python3
"""Timed Challenge #1 — Count occurrence (character in string)

Reads two lines from standard input:
1) The string
2) The character to count (if longer than 1, the first character is used)

Prints the number of occurrences (case-sensitive).
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
