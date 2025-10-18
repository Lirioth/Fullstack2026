"""
Challenges Set 1 - 20 Python Exercises
======================================
Functions, Loops, Conditionals practice with clean, commented solutions.
Covers: list manipulation, string processing, mathematical operations,
type checking, palindromes, and data structure transformations.

Author: Kevin Cusnir 'Lirioth'
Repository: Fullstack2026
Week 1 Day 5 - Mini Project
Python Version: 3.8+
"""

from typing import Any, Dict, Iterable, List, Tuple

# --------------------------
# Exercise 1
# --------------------------
def insert_at(lst: List[Any], index: int, item: Any) -> List[Any]:
    """
    Return a NEW list where `item` is inserted at position `index`.
    Does not use list.insert; we build it by slicing.
    """
    # Support negative indices similarly to Python semantics
    n = len(lst)
    if index < 0:
        index = max(0, n + index)
    if index > n:
        index = n
    return lst[:index] + [item] + lst[index:]


# --------------------------
# Exercise 2
# --------------------------
def count_spaces(s: str) -> int:
    """Count the number of space characters ' ' in a string."""
    count = 0
    for ch in s:
        if ch == ' ':
            count += 1
    return count


# --------------------------
# Exercise 3
# --------------------------
def count_case(s: str) -> Dict[str, int]:
    """
    Count uppercase and lowercase letters in s.
    Returns {'upper': U, 'lower': L}.
    """
    upper = lower = 0
    for ch in s:
        if ch.isalpha():
            if ch.isupper():
                upper += 1
            else:
                lower += 1
    return {"upper": upper, "lower": lower}


# --------------------------
# Exercise 4
# --------------------------
def my_sum(nums: Iterable[float]) -> float:
    """Sum numbers without using the built-in sum()."""
    total = 0
    for x in nums:
        total += x
    return total


# --------------------------
# Exercise 5
# --------------------------
def find_max(nums: List[float]) -> float:
    """Find the maximum value without using max()."""
    if not nums:
        raise ValueError("find_max() requires a non-empty list")
    m = nums[0]
    for x in nums[1:]:
        if x > m:
            m = x
    return m


# --------------------------
# Exercise 6
# --------------------------
def factorial(n: int) -> int:
    """Return n! for n >= 0. Uses iterative multiplication."""
    if n < 0:
        raise ValueError("factorial is undefined for negative numbers")
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result


# --------------------------
# Exercise 7
# --------------------------
def list_count(lst: List[Any], elem: Any) -> int:
    """Count occurrences of elem in lst without using .count()."""
    c = 0
    for x in lst:
        if x == elem:
            c += 1
    return c


# --------------------------
# Exercise 8
# --------------------------
def norm(nums: Iterable[float]) -> float:
    """
    Return the L2 norm: sqrt(sum(x^2 for x in nums)).
    Example: norm([1,2,2]) -> 3.0
    """
    total = 0.0
    for x in nums:
        total += (x * x)
    # avoid importing math to keep dependencies minimal
    # but since readability is nice, we can still compute sqrt via ** 0.5
    return total ** 0.5


# --------------------------
# Exercise 9
# --------------------------
def is_mono(arr: List[float]) -> bool:
    """
    True if arr is monotonic non-decreasing or non-increasing.
    Duplicates are allowed.
    """
    if len(arr) < 2:
        return True
    nondec = True
    noninc = True
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            nondec = False
        if arr[i] > arr[i - 1]:
            noninc = False
    return nondec or noninc


# --------------------------
# Exercise 10
# --------------------------
def longest_word(words: List[str]) -> str:
    """
    Return the longest word in a list.
    If there are ties, returns the first with maximal length.
    """
    if not words:
        raise ValueError("longest_word() requires a non-empty list")
    best = words[0]
    for w in words[1:]:
        if len(w) > len(best):
            best = w
    return best


# --------------------------
# Exercise 11
# --------------------------
def split_ints_and_strs(items: List[Any]) -> Tuple[List[int], List[str]]:
    """
    Given a list of integers and strings, return (ints, strs), preserving order.
    Values of other types are ignored.
    """
    ints: List[int] = []
    strs: List[str] = []
    for x in items:
        if isinstance(x, bool):
            # In Python, bool is a subclass of int; treat as neither here.
            continue
        if isinstance(x, int):
            ints.append(x)
        elif isinstance(x, str):
            strs.append(x)
    return ints, strs


# --------------------------
# Exercise 12
# --------------------------
def is_palindrome(s: str) -> bool:
    """
    Return True if s reads the same backward as forward (case-insensitive).
    Whitespace and punctuation are NOT stripped by default.
    """
    t = s.lower()
    return t == t[::-1]


# --------------------------
# Exercise 13
# --------------------------
def sum_over_k(sentence: str, k: int) -> int:
    """
    Return the number of words in the sentence with length > k.
    Words are split on whitespace using s.split() semantics.
    """
    words = sentence.split()
    c = 0
    for w in words:
        if len(w) > k:
            c += 1
    return c


# --------------------------
# Exercise 14
# --------------------------
def dict_avg(d: Dict[Any, float]) -> float:
    """Return average of the numeric values in dictionary d."""
    if not d:
        raise ValueError("dict_avg() requires a non-empty dictionary")
    total = 0.0
    count = 0
    for v in d.values():
        total += v
        count += 1
    return total / count


# --------------------------
# Exercise 15
# --------------------------
def _gcd(a: int, b: int) -> int:
    """Euclidean algorithm for greatest common divisor."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def common_div(a: int, b: int) -> List[int]:
    """
    Return the list of common divisors (excluding 1), sorted ascending.
    Example: common_div(10, 20) -> [2, 5, 10]
    """
    g = _gcd(a, b)
    if g <= 1:
        return []
    # Find divisors of g (excluding 1)
    res: List[int] = []
    i = 2
    while i * i <= g:
        if g % i == 0:
            res.append(i)
            j = g // i
            if j != i:
                res.append(j)
        i += 1
    res.append(g)  # g itself is a common divisor (>1)
    res.sort()
    return res


# --------------------------
# Exercise 16
# --------------------------
def is_prime(n: int) -> bool:
    """Return True if n is a prime number (n >= 2)."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    f = 5
    # Check up to sqrt(n) using 6k ± 1 optimization
    while f * f <= n:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True


# --------------------------
# Exercise 17
# --------------------------
def weird_print(lst: List[int]) -> List[int]:
    """
    Return elements whose index AND value are even.
    Also useful as the print target in a demo.
    Example: weird_print([1,2,2,3,4,5]) -> [2, 4]
    """
    out: List[int] = []
    for i, v in enumerate(lst):
        if i % 2 == 0 and v % 2 == 0:
            out.append(v)
    return out


# --------------------------
# Exercise 18
# --------------------------
def type_count(**kwargs: Any) -> Dict[str, int]:
    """
    Count the number of values by *exact* type in keyword arguments.
    Returns a dict like {'int': 1, 'str': 1, 'float': 1, 'bool': 2}
    Note: bool is counted separately from int.
    """
    counts: Dict[str, int] = {}
    for v in kwargs.values():
        t = type(v)
        name = t.__name__
        counts[name] = counts.get(name, 0) + 1
    return counts


# --------------------------
# Exercise 19
# --------------------------
def split_like(s: str, sep: str = None) -> List[str]:
    """
    Mimic str.split().
      - If sep is None: split on any whitespace; collapse consecutive whitespace.
      - Else: split on the exact sep (empty sep raises ValueError like str.split).
    """
    if sep is None:
        # Whitespace split with collapse
        parts: List[str] = []
        buf = ""
        in_token = False
        for ch in s:
            if ch.isspace():
                if in_token:
                    parts.append(buf)
                    buf = ""
                    in_token = False
            else:
                buf += ch
                in_token = True
        if in_token:
            parts.append(buf)
        return parts
    else:
        if sep == "":
            raise ValueError("empty separator")
        parts: List[str] = []
        start = 0
        n = len(sep)
        i = 0
        while i <= len(s):
            if s.startswith(sep, i):
                parts.append(s[start:i])
                i += n
                start = i
                continue
            i += 1
        parts.append(s[start:])
        return parts


# --------------------------
# Exercise 20
# --------------------------
def mask_password(s: str) -> str:
    """
    Convert the string into password format: same length, all '*'. 
    Note: Example in prompt shows 11 '*', but actual len('mypassword') is 10.
    """
    return '*' * len(s)


# --------------------------
# Tiny demo when run directly
# --------------------------
if __name__ == "__main__":
    print("=== Quick Demo ===")
    print("1) insert_at:", insert_at([1,2,3], 1, 99))
    print("2) count_spaces:", count_spaces("a b  c   "))
    print("3) count_case:", count_case("AbC xyz!!"))
    print("4) my_sum:", my_sum([1,5,4,2]))
    print("5) find_max:", find_max([0,1,3,50]))
    print("6) factorial:", factorial(4))
    print("7) list_count:", list_count(['a','a','t','o'],'a'))
    print("8) norm:", norm([1,2,2]))
    print("9) is_mono:", is_mono([7,6,5,5,2,0]), is_mono([2,3,3,3]), is_mono([1,2,0,4]))
    print("10) longest_word:", longest_word(['cat','kitten','bird']))
    ints, strs = split_ints_and_strs([1,'a',2,'b',True,3.5,'c',5])
    print("11) split_ints_and_strs:", ints, strs)
    print("12) is_palindrome:", is_palindrome('radar'), is_palindrome('John'))
    print("13) sum_over_k:", sum_over_k('Do or do not there is no try', 2))
    print("14) dict_avg:", dict_avg({'a':1,'b':2,'c':8,'d':1}))
    print("15) common_div:", common_div(10,20))
    print("16) is_prime:", is_prime(11), is_prime(12))
    print("17) weird_print:", weird_print([1,2,2,3,4,5]))
    print("18) type_count:", type_count(a=1,b='string',c=1.0,d=True,e=False))
    print("19) split_like:", split_like('  a  b   c '), split_like('a,b,,c,', sep=','))
    print("20) mask_password:", mask_password("mypassword"))
