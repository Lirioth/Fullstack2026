# 🥷 Exercises XP Ninja — Functions (Single File) ✨
# -------------------------------------------------
# Everything in **one** Python file, as requested.
# Language: English-only ✅
#
# 📦 Contents
#   1) get_full_name() — optional middle name + smart capitalization
#   2) text_to_morse(), morse_to_text() — English ⇄ Morse with strict validation
#   3) box_printer(*strings) — star-framed box
#   4) insertion_sort(list) — in-place, stable insertion sort + explanation
#   5) Demo runner in __main__
#
# 🚀 Quick Start
#   python3 xp_ninja_functions_single.py
#
# 🧪 Expected sample output (abridged)
#   === Exercise 1: Names ===
#   John Hooker Lee
#   Bruce Lee
#   Bruce O'Connor-Smith Lee
#
#   === Exercise 2: Morse ===
#   'SOS HELP 123' -> '... --- ... / .... . .-.. .--. / .---- ..--- ...--'
#   '... --- ... / .... . .-.. .--. / .---- ..--- ...--' -> 'SOS HELP 123'
#
#   === Exercise 3: Box ===
#   ******************
#   * Hello          *
#   * World          *
#   * in             *
#   * reallylongword *
#   * a              *
#   * frame          *
#   ******************
#
#   === Exercise 4: Insertion Sort ===
#   Before: [54, 26, 93, 17, 77, 31, 44, 55, 20]
#   After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]
#
# 📝 License
#   MIT — learn freely, remix kindly 🌱
#
# --------------------------------------
# 1) 🧑‍🤝‍🧑 get_full_name() with smart_cap
# --------------------------------------

from typing import Optional, Dict, List

def _cap_hyphen_apostrophe(token: str) -> str:
    """Capitalize a single token that may include hyphens or apostrophes.
    Example: "o'connor-smith" -> "O'Connor-Smith"
    """
    if not token:
        return token
    parts_hyphen = token.split('-')
    def cap_apostrophe(part: str) -> str:
        parts_ap = part.split("'")
        return "'".join(p.capitalize() if p else p for p in parts_ap)
    return '-'.join(cap_apostrophe(p) for p in parts_hyphen)

def smart_cap(name: str) -> str:
    """Apply smart capitalization across a string with spaces, hyphens, apostrophes.
    Example: smart_cap("  bruce  o'connor-smith  ") -> "Bruce O'Connor-Smith"
    """
    tokens = [t for t in str(name).strip().split() if t]
    return " ".join(_cap_hyphen_apostrophe(t.lower()) for t in tokens)

def get_full_name(*, first_name: str, last_name: str, middle_name: Optional[str] = None) -> str:
    """Construct a full name. `middle_name` is optional.
    Examples:
        get_full_name(first_name="john", middle_name="hooker", last_name="lee") -> 'John Hooker Lee'
        get_full_name(first_name="bruce", last_name="lee") -> 'Bruce Lee'
    """
    if first_name is None or last_name is None:
        raise ValueError("first_name and last_name are required (got None).")
    fn = smart_cap(first_name)
    ln = smart_cap(last_name)
    if not fn or not ln:
        raise ValueError("first_name and last_name must be non-empty after trimming.")
    if middle_name is None or str(middle_name).strip() == "":
        return f"{fn} {ln}"
    mn = smart_cap(middle_name)
    return f"{fn} {mn} {ln}"

# ---------------------------------------------
# 2) 📻 English ⇄ Morse: text_to_morse / back
# ---------------------------------------------

_CHAR_TO_MORSE: Dict[str, str] = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",   "E": ".",
    "F": "..-.",  "G": "--.",   "H": "....",  "I": "..",    "J": ".---",
    "K": "-.-",   "L": ".-..",  "M": "--",    "N": "-.",    "O": "---",
    "P": ".--.",  "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",  "Y": "-.--",
    "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--",
    "/": "-..-.", "(": "-.--.",  ")": "-.--.-", "&": ".-...",
    ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-",
    "_": "..--_-", '"': ".-..-.", "$": "...-..-", "@": ".--.-."
}
# Fix typo for underscore just in case
_CHAR_TO_MORSE["_"] = "..--.-"

_MORSE_TO_CHAR: Dict[str, str] = {v: k for k, v in _CHAR_TO_MORSE.items()}

def text_to_morse(text: str) -> str:
    """Convert English text to Morse code.
    Letters separated by spaces, words by ' / '.
    """
    if text is None:
        raise ValueError("text cannot be None")
    words = text.strip().split()
    encoded_words = []
    for w in words:
        codes = []
        for ch in w.upper():
            if ch not in _CHAR_TO_MORSE:
                raise ValueError(f"Unsupported character for Morse: {ch!r}")
            codes.append(_CHAR_TO_MORSE[ch])
        encoded_words.append(" ".join(codes))
    return " / ".join(encoded_words)

def morse_to_text(morse: str) -> str:
    """Convert Morse code back to English.
    Expects letters separated by spaces and words by ' / '.
    """
    if morse is None:
        raise ValueError("morse cannot be None")
    morse = morse.strip()
    if not morse:
        return ""
    words = morse.split(" / ")
    decoded_words = []
    for w in words:
        chars = w.split()
        out = []
        for code in chars:
            if code not in _MORSE_TO_CHAR:
                raise ValueError(f"Unknown Morse sequence: {code!r}")
            out.append(_MORSE_TO_CHAR[code])
        decoded_words.append("".join(out))
    return " ".join(decoded_words)

# ---------------------------------
# 3) ⭐ box_printer(*strings)
# ---------------------------------

def box_printer(*strings: str) -> str:
    """Return and print a star-framed rectangle for the given strings.
    Keeps printing for demo convenience, but also returns the frame for reuse.
    """
    lines = ["" if s is None else str(s) for s in strings]
    max_len = max((len(s) for s in lines), default=0)
    border = "*" * (max_len + 4)
    body = [f"* {s.ljust(max_len)} *" for s in lines]
    frame = "\n".join([border] + body + [border])
    print(frame)
    return frame

# ---------------------------------
# 4) 🧠 insertion_sort(list)
# ---------------------------------

def insertion_sort(alist: List[int]) -> None:
    """In-place insertion sort. Stable; best O(n), avg/worst O(n^2).
    Idea: like sorting cards in your hand — shift bigger items right, insert current.
    """
    for index in range(1, len(alist)):
        current = alist[index]
        pos = index
        while pos > 0 and alist[pos - 1] > current:
            alist[pos] = alist[pos - 1]
            pos -= 1
        alist[pos] = current

# --------------------
# 5) 🧪 Demo Runner
# --------------------

def _demo_names():
    print("\n=== Exercise 1: Names ===")
    print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))
    print(get_full_name(first_name="bruce", last_name="lee"))
    print(get_full_name(first_name="  bruce  ", middle_name=" o'connor-smith ", last_name=" LEE "))

def _demo_morse():
    print("\n=== Exercise 2: Morse ===")
    sample = "SOS HELP 123"
    encoded = text_to_morse(sample)
    decoded = morse_to_text(encoded)
    print(f"{sample!r} -> {encoded!r}")
    print(f"{encoded!r} -> {decoded!r}")

def _demo_box():
    print("\n=== Exercise 3: Box ===")
    box_printer("Hello", "World", "in", "reallylongword", "a", "frame")

def _demo_insertion_sort():
    print("\n=== Exercise 4: Insertion Sort ===")
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Before:", arr)
    insertion_sort(arr)
    print("After: ", arr)

if __name__ == "__main__":
    _demo_names()
    _demo_morse()
    _demo_box()
    _demo_insertion_sort()
