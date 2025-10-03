# Mini‑Project – Anagram Checker (All‑In‑One) ✨

This mini‑project bundles both the **logic class** and a **simple CLI** into a single file for convenience. Code is simple, commented in English, and includes friendly emojis.

---

## 📂 Files

- `anagram_checker_all.py` — Contains:
  - `AnagramChecker` class (no prints): `is_valid_word(word)`, `is_anagram(word1, word2)`, `get_anagrams(word)`
  - A tiny CLI menu with validation and formatted output.
- `words.txt` — Word list used by the checker. If it doesn’t exist, it will be **auto‑created** with a small default list that includes several known anagram families (e.g., _meat/mate/tame/team_, _listen/silent_).

> If your instructor requires **two files** (`anagram_checker.py` and `anagrams.py`), you can easily split this all‑in‑one version:
> - Move the `AnagramChecker` class into `anagram_checker.py` (unchanged).
> - Keep the UI (`main_menu`, `show_word_report`, `is_single_alpha_word`) in `anagrams.py` and `from anagram_checker import AnagramChecker`.

---

## ▶️ How to Run

```bash
python anagram_checker_all.py
```

You’ll see a simple menu:
1) Input a word  
2) Exit

Type `1`, then enter a **single alphabetic word** (no spaces, no digits, no symbols).  
The program will print:
- `YOUR WORD : "WORDINUPPERCASE"`
- Whether it is a valid English word (present in `words.txt`)
- The list of **anagrams** for that word (excluding the word itself)

---

## 🧠 How It Works

- The class loads `words.txt`, keeping a **set** for quick validity checks and a **signature index**:  
  `signature = letters of the word sorted (e.g., "meat" -> "aemt")`  
  Words with the same signature are anagrams of each other.
- `is_valid_word(word)` checks membership in the set.
- `get_anagrams(word)` looks up by signature and **excludes the original word**.
- `is_anagram(w1, w2)` compares signatures and enforces that the words differ.

---

## 📝 Customize

- Edit `words.txt` to add/remove words. You can separate by whitespace or put one word per line.  
- You can replace the fallback list entirely with your own dictionary (for example, a larger English word list).

---

## 🚀 Push to GitHub

```bash
git add -A
git commit -m "Add Anagram Checker mini-project (all-in-one) ✨"
git push
```

---

**Have fun exploring words!** 🐍🔤✨
