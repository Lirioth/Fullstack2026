"""Module: solvethematrix
Purpose: Day 4 challenge for decoding columnar matrices into clean sentences.
Author: Kevin Cusnir 'Lirioth'
Created: 2025-10-18
Last Updated: 2025-10-19

Overview:
    - Read matrices column-by-column
    - Strip non-letter noise while preserving word separation
"""

from __future__ import annotations

# 💪 Daily Challenge - Solve the Matrix
# ✅ Improved: Wrapped in main() guard and added clearer variable names

def decode_matrix(matrix_str: str) -> str:
    """
    Decode a matrix by reading column-by-column and extracting letters.
    
    Args:
        matrix_str: Multi-line string representing the matrix
        
    Returns:
        Decoded message with spaces between words
    """
    rows = [line for line in matrix_str.split("\n") if line != ""]
    cols = max(len(r) for r in rows)

    col_read = ""
    for c in range(cols):
        for r in rows:
            if c < len(r):
                col_read += r[c]

    decoded = ""
    i = 0
    n = len(col_read)
    seen_letter = False

    while i < n:
        ch = col_read[i]
        if ch.isalpha():
            decoded += ch
            seen_letter = True
            i += 1
        else:
            if not seen_letter:
                # ⚠️ Skip leading punctuation until we hit the first alphabetic character.
                i += 1
                continue
            j = i
            while j < n and not col_read[j].isalpha():
                j += 1
            if j < n:
                if decoded and decoded[-1] != " ":
                    decoded += " "
                i = j
            else:
                break
    
    return decoded


def main():
    """Run the matrix decoding challenge."""
    MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

    result = decode_matrix(MATRIX_STR)
    print(result)


if __name__ == "__main__":
    main()
