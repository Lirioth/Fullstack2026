#!/usr/bin/env python3
"""Exercises XP Ninja — Exercise 1: Cars

This script solves the tasks:
- Convert a comma-separated string of manufacturers into a list.
- Print count and descending (Z-A) order.
- Count manufacturers with 'o' (case-insensitive) and without 'i' (case-insensitive).
- Bonus: remove duplicates from a given list and print as a comma-separated string with the new count.
- Bonus: print ascending (A-Z) list but each manufacturer name reversed.
"""

def main() -> None:
    manufacturers_str = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
    manufacturers = [m.strip() for m in manufacturers_str.split(",")]

    # 1) How many manufacturers
    print(f"Total manufacturers: {len(manufacturers)}")

    # 2) Descending order (Z-A)
    desc = sorted(manufacturers, key=lambda s: s.lower(), reverse=True)
    print("Descending (Z-A):", desc)

    # 3) Counts with 'o' and without 'i' (case-insensitive)
    count_with_o = sum(1 for m in manufacturers if 'o' in m.lower())
    count_without_i = sum(1 for m in manufacturers if 'i' not in m.lower())
    print("Manufacturers with letter 'o':", count_with_o)
    print("Manufacturers without letter 'i':", count_without_i)

    # Bonus: remove duplicates from this list (preserve order)
    dupes = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
    seen = set()
    unique = []
    for m in dupes:
        if m not in seen:
            unique.append(m)
            seen.add(m)

    unique_str = ", ".join(unique)
    print("No-duplicate list:", unique_str)
    print("New total (no duplicates):", len(unique))

    # Bonus: ascending (A-Z) but reverse the letters of each manufacturer
    asc_reversed = [name[::-1] for name in sorted(manufacturers, key=lambda s: s.lower())]
    print("Ascending A-Z with reversed names:", asc_reversed)


if __name__ == "__main__":
    main()
