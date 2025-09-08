MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

rows = [line for line in MATRIX_STR.split("\n") if line != ""]
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

print(decoded)
