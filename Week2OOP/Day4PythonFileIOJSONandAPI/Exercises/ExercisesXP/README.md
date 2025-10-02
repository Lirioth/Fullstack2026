# Full-Stack Coding Bootcamp – Files & JSON XP (All-In-One) ✨

This folder includes a **single Python file** that solves both XP exercises (Random Sentence Generator + JSON) in one place, plus this README with instructions. Simple, clean, and commented in English (with friendly emojis).

---

## 📂 Files

- `xp_files_json_all.py` — All exercises combined in one script.  
  Exercises included:
  1. **Random Sentence Generator** (file handling, lists, random, validation)
  2. **Working with JSON** (parse, access nested key, modify, save)

> ℹ️ Exercise 1 originally references a **word list file**. This script will **auto-create** a minimal `words.txt` if it doesn’t exist, so it “just works.” You can edit `words.txt` to add or replace words anytime.

---

## ✅ Requirements

- Python **3.10+** recommended (no third‑party packages needed).

---

## ▶️ How to Run

From the folder that contains the files:

```bash
python xp_files_json_all.py
```

This will run a **short demo** for both exercises:
- Exercise 1 prints a random **6‑word** sentence.
- Exercise 2 loads the sample JSON, prints the **salary**, adds a `birth_date`, and saves the result to `modified_employee.json`.

---

## 🧑‍💻 Interactive Mode (Exercise 1)

The exercise specifies a `main()` that asks for user input and validates it.  
It is included in the file. If you want to use it interactively, open Python and do:

```python
from xp_files_json_all import main
main()  # follow the on-screen instructions
```

- Valid input is an **integer between 2 and 20** (inclusive).  
- The program reads words from `words.txt`. If the file is missing, it is created automatically with a small default list.

> Tip: Edit `words.txt` to include your own word list. One word per line or separated by whitespace works fine.

---

## 🔎 What You’ll See

- **Exercise 1**: A random sentence (lowercase), built from `words.txt`.  
- **Exercise 2**: Console output shows the nested **salary**, and a prettified JSON file named `modified_employee.json` is written to disk with the added `"birth_date"` field.

---

## 🚀 Pushing to GitHub

```bash
git add -A
git commit -m "Add all-in-one Files & JSON XP solutions + README ✨"
git push
```

---

**Happy coding — keep it simple and solid.** 🐍💙
