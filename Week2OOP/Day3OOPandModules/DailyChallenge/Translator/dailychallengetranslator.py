"""
File: dailychallengetranslator.py
Purpose: Single-file solution for "Daily challenge: Translator" using a translator module (googletrans). 🌍🗣️
Author: Kevin "Lirioth" Cusnir
Date: 2025-10-11 | TZ: Asia/Jerusalem

Notes:
  - Uses `googletrans` (version 4.0.0-rc1 recommended).
  - If the module/network isn't available, the script falls back to a tiny built-in mapping for the demo list. 🛟
  - Comments use emojis and stay friendly.
"""

from __future__ import annotations

from typing import Dict, Iterable, List


# Demo input (exact list from the prompt) 📋
french_words: List[str] = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]


def translate_words(words: Iterable[str], src: str = "fr", dest: str = "en") -> Dict[str, str]:
    """Translate a sequence of words from `src` to `dest` using googletrans. 🚀
    
    Returns a dict mapping original→translated.
    """
    try:
        # Import inside the function so the script can still run its fallback without the module
        from googletrans import Translator  # type: ignore
    except Exception as e:
        raise ImportError(
            "googletrans not available. Install with: pip install googletrans==4.0.0-rc1"
        ) from e

    translator = Translator()
    # googletrans can batch-translate lists ✔️
    results = translator.translate(list(words), src=src, dest=dest)
    # Ensure we handle both list-like and single result
    if not isinstance(results, list):
        results = [results]
    return {orig: res.text for orig, res in zip(words, results)}


def main() -> None:
    # Try to translate using the module; if it fails (missing package / network), use a local fallback.
    try:
        mapping = translate_words(french_words, src="fr", dest="en")
    except Exception as err:
        print("⚠️ googletrans unavailable or failed. Using a small offline fallback for the demo list.")
        # Minimal fallback just to reproduce the example output when offline ❄️
        fallback = {
            "Bonjour": "Hello",
            "Au revoir": "Goodbye",
            "Bienvenue": "Welcome",
            "A bientôt": "See you soon",
        }
        # Keep the original order
        mapping = {w: fallback.get(w, w) for w in french_words}
        print(f"Hint: To use live translation, run: pip install googletrans==4.0.0-rc1")

    # Print the dict in the same style as the example ✅
    print(mapping)


if __name__ == "__main__":
    main()
