# 💪 Daily Challenge — Challenges (Sorting & Longest Word)

Short Python solutions for two small problems: **🔤 alphabetical sorting** of a comma-separated string and **📏 finding the longest word** in a sentence.

---

## 📁 Files
- `challenges.py` — houses the reusable helpers plus an import-safe CLI runner.

### 🔍 Key Functions
- `sort_comma_separated(words: str) -> list[str]` — returns the cleaned, alphabetised tokens for Challenge 1.
- `longest_word(sentence: str) -> str` — returns the original token matching the longest alphabetic sequence.

## 🚀 How to run
```bash
python challenges.py
```
- The CLI now lives behind an `_cli()` helper so imports stay side-effect free.
- Challenge 1 prompts for the comma-separated list and prints the sorted result.
- Challenge 2 keeps the original sanity assertions; swap them for your own quick tests when needed.

---

## 1️⃣ Challenge 1 — Sorting (comma-separated words)
**🎯 Goal:** read a single comma-separated string, sort words alphabetically, and print them back joined by commas.

**🔧 Approach:**
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
- Sorting is case-sensitive by default. Pass the result through `sorted(cleaned, key=str.lower)` if you need case-insensitive ordering.

---

## Challenge 2 — Longest Word
**Goal:** return the longest token in a sentence. Punctuation like apostrophes/commas/periods counts as part of the word unless you strip it first.

**Approach:**
1. `split()` by whitespace to get tokens.
2. Strip non-letter characters with `re.sub(r"[^A-Za-z]", "", token)` before comparing lengths.
3. Track the longest original token with a simple loop (`>` ensures the **first** longest wins on ties).
4. Return `""` if the sentence is empty or contains no alphabetic characters.

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
