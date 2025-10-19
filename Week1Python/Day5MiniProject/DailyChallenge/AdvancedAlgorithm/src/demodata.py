"""
Advanced Algorithm - Data Generation Module
============================================
Random dataset generation for algorithm testing.
Provides reproducible test data with configurable size and range.
Supports seeding for deterministic results.

Author: Kevin Cusnir 'Lirioth'
Repository: Fullstack2026
Week 1 Day 5 - Mini Project
Python Version: 3.8+
"""
import random
from typing import List, Tuple

def make_dataset(n: int = 20000, low: int = 0, high: int = 10000, seed: int | None = None) -> Tuple[list[int], int]:
    """\nSummary: TODO — explain what `make_dataset` does.\n\nArgs:\n    n: TODO
        low: TODO
        high: TODO
        seed: TODO\n\nReturns:\n    TODO\n\nRaises:\n    None\n"""
    if seed is not None:
        random.seed(seed)
    nums = [random.randint(low, high) for _ in range(n)]
    target = 3728
    return nums, target
