# Challenge 1: Sorting
s = input("Enter comma-separated words: ")
parts = s.split(",")
clean = []
for w in parts:
    w = w.strip()
    if w != "":
        clean.append(w)
clean.sort()
print(",".join(clean))

# Challenge 2: Longest Word
def longest_word(sentence):
    words = sentence.split()
    if not words:
        return ""
    best = words[0]
    for w in words:
        if len(w) > len(best):
            best = w
    return best

# example calls
print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))
