"""
💪 Daily Challenge - Solve the Matrix
======================================
Column-wise matrix decoder that extracts letters and reconstructs
a clean English sentence by replacing non-letter sequences with spaces.

Author: Kevin Cusnir 'Lirioth'
Repository: Fullstack2026
Week 1 Day 4 - Functions
Python Version: 3.8+
"""

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
