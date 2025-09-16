# Daily Challenge — Challenges (Sorting & Longest Word)

Short Python solutions for two small problems: **alphabetical sorting** of a comma-separated string and **finding the longest word** in a sentence.

---

## Files
- `challenges.py` — solutions for both challenges.

## How to run
```bash
python3 challenges.py
```
- **Challenge 1** will prompt you for a comma-separated list of words.
- **Challenge 2** prints sample calls to `longest_word(...)` (you can replace them with your own tests).

---

## Challenge 1 — Sorting (comma-separated words)
**Goal:** read a single comma-separated string, sort words alphabetically, and print them back joined by commas.

**Approach:**
1. `input()` to read the string.
2. `split(",")` to get raw parts.
3. `strip()` each part and ignore empty items.
4. `list.sort()` to order the cleaned list.
5. `",".join(clean)` to print the comma-separated result.

**Example**
Input:
```
without,hello,bag,world
```
Output:
```
bag,hello,without,world
```

**Notes / Edge cases**
- Leading/trailing spaces around words are removed.
- Empty entries (e.g., double commas `a,,b`) are ignored.
- Sorting is case-sensitive by default (optional: use `clean.sort(key=str.lower)` for case-insensitive).

---

## Challenge 2 — Longest Word
**Goal:** return the longest token in a sentence. Punctuation like apostrophes/commas/periods counts as part of the word.

**Approach:**
1. `split()` by whitespace to get tokens.
2. Track the longest token with a simple loop (`>` ensures the **first** longest wins on ties).
3. Return `""` if the sentence is empty.

**Examples**
```python
longest_word("Margaret's toy is a pretty doll.")     # -> "Margaret's"
longest_word("A thing of beauty is a joy forever.")  # -> "forever."
longest_word("Forgetfulness is by all means powerless!")  # -> "Forgetfulness"
```

**Optional tweaks**
- One-liner: `max(words, key=len)` (keeps the first max on ties).
- Strip only *trailing* punctuation if desired (changes the spec).

---

## Complexity
- Sorting N words: **O(N log N)** time, O(N) space.
- Longest word scan: **O(M)** in number of tokens.

---

## Testing
Replace the sample calls at the bottom with your own sentences, or wrap them in `if __name__ == "__main__":` for more control.
