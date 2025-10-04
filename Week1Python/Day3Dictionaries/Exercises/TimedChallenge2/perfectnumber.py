#!/usr/bin/env python3
"""Timed Challenge #2 — Perfect Number

Reads an integer from input and prints True if it is a perfect number,
else prints False. A perfect number equals the sum of its proper divisors
(positive divisors excluding the number itself).

Examples
Input : 6   -> True   (1 + 2 + 3 = 6)
Input : 10  -> False  (1 + 2 + 5 = 8)
"""

import sys
import math

def is_perfect(n: int) -> bool:
    if n <= 1:
        return False
    total = 1  # 1 is a proper divisor of any n > 1
    limit = int(math.isqrt(n))
    for i in range(2, limit + 1):
        if n % i == 0:
            total += i
            other = n // i
            if other != i:  # avoid double-counting squares
                total += other
        if total > n:
            # Small early exit: if sum already exceeds n, it cannot be perfect
            return False
    return total == n

def main() -> None:
    try:
        x = int(input('Enter the Number:'))
    except Exception:
        # If parsing fails, follow the spec to output boolean only
        print(False)
        return
    print(is_perfect(x))

if __name__ == '__main__':
    main()
