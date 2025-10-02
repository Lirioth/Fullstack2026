# xp_files_json_all.py
# 💡 Full-Stack Coding Bootcamp - Files & JSON XP (All In One)
# -----------------------------------------------------------
# This single Python file contains solutions for these exercises:
# 1) Random Sentence Generator (reads words from a file, validates input) 📄🎲
# 2) Working with JSON (parse, access nested key, modify, save) 🧩🔐
#
# 📝 Notes:
# - Comments are in English and include emojis for friendliness.
# - Code stays simple and readable.
# - Exercise 1 originally expects an interactive `main()` — it is provided here.
#   For convenience, a `run_all_demos()` is also provided and called by default.
#
# Run:
#   python xp_files_json_all.py
#
# Enjoy! 🐍💙


from __future__ import annotations
import json
import random
from pathlib import Path


# ----------------------------------------------------
# 🌟 Exercise 1: Random Sentence Generator
# ----------------------------------------------------

# ✅ Default words used if "words.txt" is missing. Kept small & simple.
_DEFAULT_WORDS = (
    "sun moon star sky cloud wind rain river ocean mountain valley forest "
    "light shadow fire stone sand leaf tree flower grass road path way "
    "dream heart mind soul time life world power peace sound voice song "
    "code logic bug test build ship learn grow focus strong brave calm"
).split()


def get_words_from_file(filepath: str | Path) -> list[str]:
    """Read a list of words from a file. Returns a list of words (strings). 📄
    If the file does not exist, it will be created with a simple default list. ✨
    """
    path = Path(filepath)
    if not path.exists():
        # 🧯 Safety net: create a simple words.txt so the program always works
        path.write_text("\n".join(_DEFAULT_WORDS), encoding="utf-8")
        # (We do not raise here — we just created it.)

    # 📖 Read file and split by any whitespace
    text = path.read_text(encoding="utf-8")
    words = text.split()
    return words


def get_random_sentence(length: int, words_file: str | Path = "words.txt") -> str:
    """Generate a random sentence with `length` words from a file. 🎲🧠
    The sentence is returned in lowercase, words separated by a single space.
    """
    words = get_words_from_file(words_file)

    # 🧪 Basic defensive check: ensure we have words available
    if not words:
        # If the file somehow ended up empty, fall back to the default list
        words = list(_DEFAULT_WORDS)

    # 🎯 Choose `length` random words and join
    chosen = [random.choice(words) for _ in range(length)]
    sentence = " ".join(chosen).lower()
    return sentence


def main():
    """Interactive main for Exercise 1: ask for sentence length and print. 🧑‍💻
    Validates integer input between 2 and 20 (inclusive).
    """
    print("Welcome! This program generates a random sentence from a word list. ✨")
    print("You can adjust the word list by editing 'words.txt' in this folder. 📝\n")
    try:
        raw = input("Enter sentence length (an integer between 2 and 20): ").strip()
        length = int(raw)
    except ValueError:
        print("❌ Invalid input: please enter an integer (e.g., 5).")
        return

    # ✅ Validate range
    if not (2 <= length <= 20):
        print("❌ Length must be between 2 and 20 (inclusive).")
        return

    # ✅ Generate and print
    sentence = get_random_sentence(length, words_file="words.txt")
    print(f"\nYour random sentence:\n📝 {sentence}")


# ----------------------------------------------------
# 🌟 Exercise 2: Working with JSON
# ----------------------------------------------------

_SAMPLE_JSON = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


def process_employee_json(output_path: str | Path = "modified_employee.json",
                          birth_date: str = "2000-01-01") -> None:
    """Parse sample JSON, access nested salary, add 'birth_date', and save. 🧩💾
    - Prints the salary.
    - Adds 'birth_date' to the employee dict.
    - Saves the modified JSON into `output_path` with indentation.
    """
    # 🔓 Load/parse JSON
    data = json.loads(_SAMPLE_JSON)

    # 🧭 Access nested salary
    salary = data["company"]["employee"]["payable"]["salary"]
    print(f"Employee salary is: {salary} 💰")

    # ➕ Add 'birth_date' to the employee dictionary
    data["company"]["employee"]["birth_date"] = birth_date

    # 💾 Save to a JSON file (pretty printed)
    out = Path(output_path)
    with out.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Modified JSON saved to: {out.resolve()} ✅")


# -----------------------
# 🧪 Demo runner (simple)
# -----------------------

def run_all_demos():
    # 🎲 Exercise 1 (non-interactive demo): generate a 6-word sentence
    print("===== Exercise 1: Random Sentence (demo length=6) =====")
    sentence = get_random_sentence(6, words_file="words.txt")
    print(f"📝 {sentence}\n")

    # 🧩 Exercise 2: JSON processing with a sample birth date
    print("===== Exercise 2: JSON Access/Modify/Save =====")
    process_employee_json(output_path="modified_employee.json", birth_date="1994-06-16")


if __name__ == "__main__":
    # 🚀 Run demos by default.
    # To use the interactive prompt for Exercise 1, call `main()` instead.
    run_all_demos()
