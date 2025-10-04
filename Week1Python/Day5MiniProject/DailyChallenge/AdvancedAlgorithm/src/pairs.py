"""
Efficient pair-finding for target sums.
We expose:
- find_value_pairs_hash: O(n) using Counter (unique value pairs + total index-pair count)
- find_value_pairs_two_pointer: O(n log n) unique value pairs via sorting
"""
from collections import Counter
from typing import Iterable, List, Tuple

def find_value_pairs_hash(nums: Iterable[int], target: int) -> tuple[list[tuple[int, int]], int]:
    """
    Return (pairs, total_index_pairs):
      - pairs: sorted list of unique value pairs (a, b) with a <= b
      - total_index_pairs: total # of index pairs implied by multiplicities (combinatorial count)
    """
    counts = Counter(nums)
    pairs: list[tuple[int, int]] = []
    total_index_pairs = 0
    for a in sorted(counts):
        b = target - a
        if b not in counts:
            continue
        if a < b:
            pairs.append((a, b))
            total_index_pairs += counts[a] * counts[b]
        elif a == b:
            c = counts[a]
            if c >= 2:
                pairs.append((a, b))
                total_index_pairs += c * (c - 1) // 2
        # if a > b, skip to avoid duplicate pairs
    return pairs, total_index_pairs

def find_value_pairs_two_pointer(nums: Iterable[int], target: int) -> list[tuple[int, int]]:
    """
    Return the list of unique value pairs (a, b) with a <= b using a sorted two-pointer scan.
    Note: does not compute multiplicity counts.
    """
    arr = sorted(nums)
    i, j = 0, len(arr) - 1
    pairs: list[tuple[int, int]] = []
    last = None
    while i <= j:
        s = arr[i] + arr[j]
        if s == target:
            a, b = arr[i], arr[j]
            if last != (a, b):
                pairs.append((a, b))
                last = (a, b)
            # move both pointers, skipping duplicates
            ai, bj = a, b
            while i <= j and arr[i] == ai: i += 1
            while i <= j and arr[j] == bj: j -= 1
        elif s < target:
            i += 1
        else:
            j -= 1
    return pairs
