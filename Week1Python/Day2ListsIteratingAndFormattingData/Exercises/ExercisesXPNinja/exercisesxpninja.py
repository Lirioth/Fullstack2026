# Exercises XP Ninja

# ---------- Exercise 1: Formula ----------
# Q = sqrt((2 * C * D) / H), C=50, H=30
import math

data = input("Enter D values (comma-separated): ")  # e.g. 100,150,180
Ds = [x.strip() for x in data.split(",") if x.strip() != ""]
C, H = 50, 30
results = []
for d in Ds:
    D = int(d)
    q = int(round(math.sqrt((2 * C * D) / H)))
    results.append(str(q))
print(",".join(results))   # e.g. 18,22,24

# ---------- Exercise 2: List of integers ----------
# use one example list
nums = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]

# 2a) print list in one line
print("list:", " ".join(str(x) for x in nums))

# 2b) sorted desc
print("desc:", " ".join(str(x) for x in sorted(nums, reverse=True)))

# 2c) sum
print("sum:", sum(nums))

# 3) first and last
print("first+last:", [nums[0], nums[-1]])

# 4) > 50
print(">50:", [x for x in nums if x > 50])

# 5) < 10
print("<10:", [x for x in nums if x < 10])

# 6) squares
print("squares:", " ".join(str(x*x) for x in nums))

# 7) no duplicates + count
no_dups = []
for x in nums:
    if x not in no_dups:
        no_dups.append(x)
print("no_dups:", no_dups, "count:", len(no_dups))

# 8) average
print("avg:", sum(nums) / len(nums))

# 9) largest
print("max:", max(nums))

# 10) smallest
print("min:", min(nums))

# 11) Bonus: sum, avg, max, min without built-ins
s = 0
mx = nums[0]
mn = nums[0]
for x in nums:
    s += x
    if x > mx: mx = x
    if x < mn: mn = x
print("manual sum:", s, "manual avg:", s/len(nums), "manual max:", mx, "manual min:", mn)

# ---------- Exercise 3: Working on a paragraph ----------
para = (
    "Learning Python is fun. It helps you think clearly! "
    "Python has simple syntax, yet it is powerful. Keep practicing?"
)

# characters (with spaces)
chars = len(para)

# sentences: count ., !, ?
sentences = para.count(".") + para.count("!") + para.count("?")
if sentences == 0:
    sentences = 1  # avoid division by zero

# words (split on whitespace)
words = para.split()
word_count = len(words)

# unique words (lowercased, strip simple punctuation)
cleaned = []
for w in words:
    cleaned.append(w.strip(".,!?;:").lower())
unique_words = set(cleaned)
unique_count = len(unique_words)

# bonus: non-whitespace chars
non_ws = sum(1 for ch in para if not ch.isspace())

# bonus: average words per sentence
avg_w_per_sent = word_count / sentences

# bonus: number of non-unique words (words that appear more than once)
from collections import Counter
freq = Counter(cleaned)
non_unique_total = sum(c for c in freq.values() if c > 1)

print("chars:", chars)
print("sentences:", sentences)
print("words:", word_count)
print("unique words:", unique_count)
print("non-whitespace chars:", non_ws)
print("avg words/sentence:", round(avg_w_per_sent, 2))
print("non-unique words total count:", non_unique_total)

# ---------- Exercise 4: Frequency Of The Words ----------
text = input("Enter a line for word frequency: ")
tokens = text.split()  # keep punctuation attached, case-sensitive (like the example)
from collections import Counter
counts = Counter(tokens)
for token in sorted(counts.keys()):
    print(f"{token}:{counts[token]}")
