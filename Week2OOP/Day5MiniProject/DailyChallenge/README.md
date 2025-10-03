# 🏆 Daily Challenge – Build the Anagram Checker

The Day 5 daily challenge is identical to the mini-project: create a playful yet well-structured **Anagram Checker**. This README now mirrors the canonical instructions in [`README_ANAGRAMS.md`](README_ANAGRAMS.md) so you always land on the correct guidance.

> ✨ Looking for the story-style walkthrough? Jump directly to [`README_ANAGRAMS.md`](README_ANAGRAMS.md). Everything below is a concise summary.

---

## 🎯 Challenge Goals

1. Implement the `AnagramChecker` class that:
   - Loads words from `words.txt` into fast lookup structures.
   - Validates whether a string is a real word.
   - Finds all anagrams for a given word, excluding the word itself.
2. Provide a lightweight CLI inside [`anagram_checker_all.py`](anagram_checker_all.py) that:
   - Presents a simple menu (enter a word / exit).
   - Ensures the user input is a single alphabetical word.
   - Displays validation results and any discovered anagrams.

All required logic and the menu already live together in `anagram_checker_all.py`, making it easy to review and extend.

---

## ▶️ Run the Challenge

```bash
cd Week2OOP/Day5MiniProject/DailyChallenge
python anagram_checker_all.py
```

You should see output similar to the screenshot described in the main README_ANAGRAMS guide: the program echoes the uppercase version of your word, states if it is valid, and lists its anagrams.

---

## 🛠️ Want to Extend It?

`README_ANAGRAMS.md` includes ideas for:

- Splitting the all-in-one script into `anagram_checker.py` (logic) and `anagrams.py` (CLI).
- Swapping in a larger dictionary for `words.txt`.
- Adding unit tests or alternative interfaces.

Treat those as stretch goals once you understand the baseline solution.

---

## ✅ Deliverable Checklist

- [ ] Review `README_ANAGRAMS.md` to understand the project expectations.
- [ ] Run `anagram_checker_all.py` and test several valid and invalid words.
- [ ] Capture notes or screenshots if your instructor asks for proof of completion.

Have fun discovering new anagrams! 🔤🐍
