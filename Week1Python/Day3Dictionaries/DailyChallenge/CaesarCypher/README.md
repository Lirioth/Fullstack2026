
# Daily Challenge GOLD — Caesar Cipher 🔐🧠

A clean Python implementation of the **Caesar cipher** with **encrypt**, **decrypt**, and **brute-force** modes.

## ✅ Features
- Shifts letters with wrap‑around (A↔Z, a↔z), preserves case.
- Leaves non‑letters (spaces, punctuation, digits) unchanged.
- Works **interactively** or with **CLI flags**.
- Accepts positive or negative shifts.

## ▶️ Run (interactive)
```bash
python caesar_cipher.py
```
Then choose: **E**ncrypt / **D**ecrypt / **B**rute‑force / **Q**uit.

## ▶️ Run (CLI)
```bash
# Encrypt
python caesar_cipher.py --mode encrypt --shift 3 --text "Hello, World!"
# -> Khoor, Zruog!

# Decrypt
python caesar_cipher.py --mode decrypt --shift 3 --text "Khoor, Zruog!"
# -> Hello, World!

# Brute-force (unknown shift)
python caesar_cipher.py --mode brute --text "Khoor, Zruog!"
```

## 🧪 How it works
For each letter: convert to a 0–25 index, add the shift, wrap modulo 26, and convert back. Non‑letters pass through untouched.

## 📝 File
- `caesar_cipher.py` — single‑file solution (no external deps).

Have fun encrypting like Julius Caesar! 🏺
