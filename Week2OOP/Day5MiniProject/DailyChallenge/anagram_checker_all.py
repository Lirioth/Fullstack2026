# anagram_checker_all.py
# 💡 Mini‑Project: Anagram Checker (All In One)
# -------------------------------------------------
# Contains both:
# 1) AnagramChecker class (logic, no prints) 🧠
# 2) Simple CLI UI menu (prints) 🖥️
#
# Comments are in English with emojis. Code kept simple and readable.
#
# Run:
#   python anagram_checker_all.py
#
# Optional:
# - Provide your own "words.txt" in the same folder (one word per line OR whitespace-separated).
# - If "words.txt" is missing, a small default list will be created automatically.
#
# Enjoy! 🐍✨

from __future__ import annotations
from pathlib import Path
from collections import defaultdict

# ------------------------------
# 🔤 Word list fallback (small)
# ------------------------------
# This list is used to auto-create a basic "words.txt" if missing.
# It includes common anagram families for demo purposes.
_FALLBACK_WORDS = """
meat mate tame team
listen silent enlist tinsel inlets
read dear dare
evil live veil vile
stone tones seton onest
night thing
alert alter later
angle glean angel
below elbow
state taste
parts strap sprat
dusty study
cinema iceman
save vase
sadder dreads
rescue secure recuse
earth heart hater
fluster restful
santa satan
credit direct
god dog
cat act
rat tar
note tone
scar cars arcs
inch chin
brag grab
blue lube
care race
tab bat
stressed desserts
"""


def ensure_words_file(path: str | Path = "words.txt") -> Path:
    """Ensure a 'words.txt' exists. If missing, create it with a small fallback list. ✨"""
    p = Path(path)
    if not p.exists():
        p.write_text(_FALLBACK_WORDS.strip() + "\n", encoding="utf-8")
    return p


# -----------------------------------
# 🌟 Part 1: AnagramChecker (no I/O)
# -----------------------------------

class AnagramChecker:
    """Encapsulates anagram logic. Does not print. 🧠"""

    def __init__(self, wordlist_path: str | Path = "words.txt"):
        """Load words from file into fast lookup structures. 🚀
        - A set for quick validity checks.
        - A signature map: sorted letters -> set of words.
        """
        self.wordlist_path = Path(wordlist_path)
        text = self.wordlist_path.read_text(encoding="utf-8")

        # Split on whitespace; keep only alphabetic tokens; store lowercase
        words = [w.strip().lower() for w in text.split() if w.strip().isalpha()]

        # ✅ Public-like structures (but internal use): a set, and a signature index
        self._words_set = set(words)
        self._sig_to_words = defaultdict(set)  # signature -> set[str]

        for w in self._words_set:
            sig = self._signature(w)
            self._sig_to_words[sig].add(w)

    # --------------------
    # 🔧 Helper utilities
    # --------------------
    @staticmethod
    def _normalize(word: str) -> str:
        """Lowercase and strip surrounding whitespace. 🧼"""
        return word.strip().lower()

    @staticmethod
    def _signature(word: str) -> str:
        """Return a canonical signature for the word (sorted letters). 🧬"""
        return "".join(sorted(word))

    # -----------------------
    # ✅ Public API (no I/O)
    # -----------------------
    def is_valid_word(self, word: str) -> bool:
        """Return True if `word` is a valid English word from the list. ✅"""
        w = self._normalize(word)
        return w.isalpha() and w in self._words_set

    def is_anagram(self, word1: str, word2: str) -> bool:
        """Return True if word1 and word2 have the same letters (different order). 🔁"""
        w1, w2 = self._normalize(word1), self._normalize(word2)
        if w1 == w2:
            return False  # not considered an anagram of itself
        if not (w1.isalpha() and w2.isalpha()):
            return False
        return self._signature(w1) == self._signature(w2)

    def get_anagrams(self, word: str) -> list[str]:
        """Return a list of all anagrams for `word` (excluding the word itself). 📜"""
        w = self._normalize(word)
        if not w.isalpha():
            return []
        sig = self._signature(w)
        candidates = self._sig_to_words.get(sig, set())
        # Exclude the original word itself
        result = sorted([cand for cand in candidates if cand != w])
        return result


# ---------------------------------
# 🌟 Part 2: Simple CLI (with I/O)
# ---------------------------------

def is_single_alpha_word(user_input: str) -> bool:
    """Return True if the input is a single alphabetic word (no spaces, digits, or symbols). ✅"""
    s = user_input.strip()
    # exactly one token and only letters
    return len(s.split()) == 1 and s.isalpha()


def show_word_report(checker: AnagramChecker, word: str) -> None:
    """Pretty-print the word info using AnagramChecker (UI-level function). 🎨"""
    upper = word.strip().upper()
    print(f'\nYOUR WORD : "{upper}"')
    if checker.is_valid_word(word):
        print("this is a valid English word.")
    else:
        print("this is NOT a valid English word.")

    anas = checker.get_anagrams(word)
    if anas:
        print("Anagrams for your word: " + ", ".join(anas) + ".")
    else:
        print("Anagrams for your word: none found.")


def main_menu() -> None:
    """Loop a simple menu until user exits. 🖥️"""
    # Ensure there's a words file available
    words_path = ensure_words_file("words.txt")

    # Create the checker (loads the words)
    checker = AnagramChecker(words_path)

    while True:
        print("\n=== ANAGRAM CHECKER ===")
        print("1) Input a word")
        print("2) Exit")
        choice = input("Choose an option (1/2): ").strip().lower()

        if choice in {"2", "q", "quit", "exit"}:
            print("Goodbye! 👋")
            break
        if choice not in {"1"}:
            print("❌ Invalid choice. Please select 1 or 2.")
            continue

        # Ask for a word
        user_word = input("Type a single English word (letters only): ").strip()

        # Validate basic UI constraints
        if not is_single_alpha_word(user_word):
            print("❌ Error: Please enter exactly ONE word made of letters only (no spaces, digits, or symbols).")
            continue

        # Show the formatted report
        show_word_report(checker, user_word)


if __name__ == "__main__":
    # Run the menu app
    main_menu()
