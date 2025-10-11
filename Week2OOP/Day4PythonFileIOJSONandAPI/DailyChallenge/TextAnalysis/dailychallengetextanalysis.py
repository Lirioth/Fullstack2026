"""
File: dailychallengetextanalysis.py
Purpose: Daily Challenge — Text Analysis (OOP + file handling + regex) 📚🧠
Author: Kevin "Lirioth" Cusnir
Date: 2025-10-11 | TZ: Asia/Jerusalem

Includes:
  • Text — analyze raw text (word frequency, most common word, unique words, from_file).
  • TextModification — inherits from Text; cleans text (punctuation, stop words, special chars).

Notes:
  - Comments contain emojis (per request) 👍
  - Methods mutate `self.text` only in TextModification cleaners (and also return the new text). 🧼
"""

from __future__ import annotations

import re
import string
from collections import Counter
from dataclasses import dataclass
from typing import ClassVar, Dict, Iterable, List, Optional, Set


# =========================
# Part I — Text analysis 🔍
# =========================
@dataclass
class Text:
    """Analyze text content from a string or file. 🧪"""

    text: str

    # ---------- Utilities ----------
    _word_re: ClassVar[re.Pattern] = re.compile(r"[A-Za-z0-9']+")  # keep words like don't, O'Neill, and numbers 🧩

    def _tokenize(self) -> List[str]:
        """Tokenize to lowercase word list using regex. 🧰
        Example: "Hello, world!" -> ["hello", "world"]
        """
        # Lowercase to make counting case-insensitive 🧯
        return [w.lower() for w in self._word_re.findall(self.text)]

    # ---------- Step 2 ----------
    def word_frequency(self, word: str) -> Optional[int]:
        """Return how many times `word` appears (case-insensitive). If absent, return None. 🔢"""
        if not word:
            return None
        tokens = self._tokenize()
        word_lc = word.lower()
        count = sum(1 for w in tokens if w == word_lc)
        return count if count > 0 else None

    # ---------- Step 3 ----------
    def most_common_word(self) -> Optional[str]:
        """Return the most frequent word (case-insensitive). If no words, None. 🥇"""
        tokens = self._tokenize()
        if not tokens:
            return None
        most = Counter(tokens).most_common(1)[0][0]
        return most

    # ---------- Step 4 ----------
    def unique_words(self) -> List[str]:
        """Return a sorted list of unique words (case-insensitive). 🧭"""
        tokens = self._tokenize()
        return sorted(set(tokens))

    # ---------- Part II / Step 5 ----------
    @classmethod
    def from_file(cls, file_path: str, *, encoding: str = "utf-8") -> "Text":
        """Create a Text from a file's contents. 📂"""
        with open(file_path, "r", encoding=encoding) as f:
            data = f.read()
        return cls(data)


# ==============================
# Bonus — Text modifications 🧼
# ==============================
class TextModification(Text):
    """Cleaning utilities extending Text. 🧽"""

    # A compact, practical stop-word list (common English function words). 🧱
    DEFAULT_STOP_WORDS: ClassVar[Set[str]] = {
        "a","an","and","the","is","are","am","be","been","being","to","of","in","on","for","with","as",
        "by","at","from","that","this","these","those","it","its","itself","if","else","but","or","so",
        "because","about","into","through","during","before","after","above","below","up","down","out",
        "over","under","again","further","then","once","here","there","when","where","why","how","all",
        "any","both","each","few","more","most","other","some","such","no","nor","not","only","own",
        "same","than","too","very","can","will","just","don","should","now","i","you","he","she","we",
        "they","me","him","her","us","them","my","your","his","their","our","yours","hers","ours","theirs"
    }

    def remove_punctuation(self) -> str:
        """Remove ASCII punctuation characters using translate(). ✂️
        Keeps letters, digits, whitespace, and non-ASCII letters intact.
        """
        table = str.maketrans("", "", string.punctuation)
        self.text = self.text.translate(table)
        return self.text

    def remove_stop_words(self, stop_words: Optional[Iterable[str]] = None) -> str:
        """Remove stop words (case-insensitive), preserving original non-stop tokens. 🧹"""
        stops = set((stop_words or self.DEFAULT_STOP_WORDS))
        tokens = self._tokenize()
        # Map tokens to original slices for minimal distortion: rebuild using simple join. 🧵
        kept = [t for t in tokens if t not in stops]
        self.text = " ".join(kept)
        return self.text

    def remove_special_characters(self, keep_basic_punct: bool = False) -> str:
        """Remove special characters via regex. 🧯
        If keep_basic_punct=True, keep .,!?;:'- and whitespace; else keep only word chars + whitespace.
        """
        if keep_basic_punct:
            self.text = re.sub(r"[^\w\s\.,!\?;:'\-]", "", self.text, flags=re.UNICODE)
        else:
            self.text = re.sub(r"[^\w\s]", "", self.text, flags=re.UNICODE)
        return self.text


# ==============
# Tiny demos ✅
# ==============
if __name__ == "__main__":
    sample = "Hello, hello! This is a tiny test. Isn't it lovely? Hello again."
    print("=== Demo: Text ===")
    t = Text(sample)
    print("word_frequency('hello') ->", t.word_frequency("hello"))       # 3
    print("most_common_word() ->", t.most_common_word())                 # 'hello'
    print("unique_words() ->", t.unique_words())                         # sorted unique list

    print("
=== Demo: TextModification ===")
    tm = TextModification(sample)
    print("remove_punctuation() ->", tm.remove_punctuation())
    tm = TextModification(sample)  # reset
    print("remove_stop_words() ->", tm.remove_stop_words())
    tm = TextModification(sample)  # reset
    print("remove_special_characters(keep_basic_punct=True) ->", tm.remove_special_characters(keep_basic_punct=True))
