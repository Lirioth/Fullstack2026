"""
Starter data generation that mirrors the prompt.
Use --seed to make results reproducible.
"""
import random
from typing import List, Tuple

def make_dataset(n: int = 20000, low: int = 0, high: int = 10000, seed: int | None = None) -> Tuple[list[int], int]:
    if seed is not None:
        random.seed(seed)
    nums = [random.randint(low, high) for _ in range(n)]
    target = 3728
    return nums, target
