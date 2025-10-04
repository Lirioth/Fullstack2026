"""
Exercise 1 — Draw patterns with for-loops.
All functions return the multi-line string and also print it for demo convenience.
"""

def pattern_a() -> str:
    """
      *
     ***
    *****
    Height is 3; centered pyramid of odd stars (1, 3, 5).
    """
    h = 3
    lines = []
    for i in range(1, h + 1):
        spaces = " " * (h - i)
        stars = "*" * (2 * i - 1)
        lines.append(spaces + stars)
    out = "\n".join(lines)
    print(out)
    return out

def pattern_b() -> str:
    """
        *
       **
      ***
     ****
    *****
    Right-aligned triangle of height 5.
    """
    h = 5
    lines = []
    for i in range(1, h + 1):
        spaces = " " * (h - i)
        stars = "*" * i
        lines.append(spaces + stars)
    out = "\n".join(lines)
    print(out)
    return out

def pattern_c() -> str:
    r"""
    *
    **
    ***
    ****
    *****
    *****
     ****
      ***
       **
        *
    Mixed: left-aligned increasing triangle up to 5, repeat the top row,
    then a right-shifted decreasing triangle.
    """
    up_h = 5
    lines = []
    # Increasing (left-aligned)
    for i in range(1, up_h + 1):
        lines.append("*" * i)
    # Repeat the top
    lines.append("*" * up_h)
    # Decreasing (right-shifted)
    for i in range(up_h - 1, 0, -1):
        pad = " " * (up_h - i)
        lines.append(pad + ("*" * i))
    out = "\n".join(lines)
    print(out)
    return out

if __name__ == "__main__":
    print("=== Pattern A ===")
    pattern_a()
    print("\n=== Pattern B ===")
    pattern_b()
    print("\n=== Pattern C ===")
    pattern_c()
