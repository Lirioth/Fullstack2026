import re


# Challenge 1: Sorting 🧩
s = input("Enter comma-separated words: ")
parts = s.split(",")
clean = []
for w in parts:
    w = w.strip()
    if w != "":
        clean.append(w)
if clean:
    clean.sort()
    print(",".join(clean))
else:
    print("No valid words were provided 🤖")


# Challenge 2: Longest Word 🧠
def longest_word(sentence):
    words = sentence.split()
    best = ""
    longest_length = 0
    for w in words:
        cleaned = re.sub(r"[^A-Za-z]", "", w)
        if not cleaned:
            continue
        if len(cleaned) > longest_length:
            best = w
            longest_length = len(cleaned)
    return best


if __name__ == "__main__":
    # Quick sanity checks 🤖
    assert longest_word("Margaret's toy is a pretty doll.") == "Margaret's"
    assert longest_word("A thing of beauty is a joy forever.") == "forever."
    assert longest_word("Forgetfulness is by all means powerless!") == "Forgetfulness"
    assert longest_word("Wow!!! So??? yes.") == "Wow!!!"
    assert longest_word("!!! 123 ...") == ""
