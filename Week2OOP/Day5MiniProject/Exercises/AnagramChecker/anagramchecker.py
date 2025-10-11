"""
File: anagramchecker.py
Purpose: Core logic for the Anagram Checker mini‑project. 🧠🔤
Note: This module prints nothing; it exposes a clean OOP API for the UI. ✅
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Set


def _normalize(word: str) -> str:
    """Normalize a token to uppercase alphabetic letters only. 🧼🔠"""
    return "".join(ch for ch in word.strip() if ch.isalpha()).upper()


def _signature(word: str) -> str:
    """Return the sorted‑letters signature for a word (e.g., MEAT -> AEMT). 🧾"""
    return "".join(sorted(_normalize(word)))


@dataclass
class AnagramChecker:
    """Loads a word list and answers anagram queries. 📚✨"""
    wordlist_path: str = "words.txt"
    words: Set[str] = field(init=False, default_factory=set)         # all valid words (UPPERCASE) 📖
    index: Dict[str, List[str]] = field(init=False, default_factory=dict)  # signature -> words 🗂️

    def __post_init__(self) -> None:
        self._load_words(self.wordlist_path)
        self._build_index()

    # ------------- loading & indexing -------------
    def _load_words(self, path: str) -> None:
        """Load words from a file (one per line). Non‑letters stripped; stored UPPERCASE. 📥"""
        self.words.clear()
        try:
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    tok = _normalize(line)
                    if tok:
                        self.words.add(tok)
        except FileNotFoundError:
            # Optional fallback to a system dictionary path (best effort). 🛟
            fallback = "/usr/share/dict/words"
            try:
                with open(fallback, "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        tok = _normalize(line)
                        if tok:
                            self.words.add(tok)
            except Exception:
                # Leave set empty; UI may inform the user about missing list. 🚫
                self.words = set()

    def _build_index(self) -> None:
        """Map each signature to its word bucket for fast anagram lookup. ⚡"""
        self.index.clear()
        for w in self.words:
            sig = _signature(w)
            self.index.setdefault(sig, []).append(w)
        # Keep buckets sorted for deterministic output. 🧩
        for bucket in self.index.values():
            bucket.sort()

    # ------------- API -------------
    def is_valid_word(self, word: str) -> bool:
        """True iff word is alphabetic and present in the word list (case‑insensitive). ✅"""
        norm = _normalize(word)
        return bool(norm) and norm in self.words

    def is_anagram(self, word1: str, word2: str) -> bool:
        """True if words are different (ignoring case) but share the same signature. 🔁"""
        w1, w2 = _normalize(word1), _normalize(word2)
        return bool(w1 and w2) and (w1 != w2) and (_signature(w1) == _signature(w2))

    def get_anagrams(self, word: str) -> List[str]:
        """Return sorted anagrams of `word` excluding the word itself (case‑insensitive). 🧮"""
        norm = _normalize(word)
        if not norm:
            return []
        bucket = self.index.get(_signature(norm), [])
        # Exclude self (case‑insensitive), keep original casing as UPPER for consistency. 🚫
        return [w for w in bucket if w != norm]
