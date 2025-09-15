# Daily Challenge GOLD — Happy Birthday

A tiny Python script that asks for your **birthdate**, prints your **age**, and draws a cute ASCII **birthday cake** with candles equal to the **last digit** of your age. If you were **born in a leap year**, it prints **two cakes** (bonus!).

## 🎯 What it does (step by step)
1. **Asks for your birthdate** in the format `DD/MM/YYYY` (example: `16/06/1994`).
2. **Parses** it with `datetime.strptime(...)` and converts to a `date`.
3. **Computes your age** as of **today** (using a common year-difference trick with month/day comparison).
4. **Sets candles** to `age % 10` (the last digit of your age).
   - Example: age **31** → `31 % 10 == 1` → **1 candle**.
   - Example: age **40** → `40 % 10 == 0` → **0 candles** (top row has no `i`).  
5. **Draws the cake** with a small ASCII art. The top line shows the candles as repeated `i` characters.
6. **Leap-year bonus**: if your **birth year** is a leap year (`calendar.isleap(bday.year)`), it prints the cake **twice**.

## 🧁 Example (output shape)
If `candles = 3`, the top looks like:
```
       ___iii___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
```

> Note: The script uses **your system date** for “today”, so running on a different day changes the age/candles.

## ▶️ How to run
### Option A — Double click (if `.py` is associated to Python on your OS)
- Save the file as `happy_birthday.py` and double click.

### Option B — Terminal / Command Prompt
```bash
# macOS / Linux
python3 happy_birthday.py

# Windows
python happy_birthday.py
# or
py happy_birthday.py
```
When prompted, type your birthdate as `DD/MM/YYYY` and press Enter.

## 🛡️ Error handling (optional improvement)
Right now, if the format is wrong, `strptime` raises a `ValueError`. You can make it friendlier:
```python
while True:
    s = input("Enter your birthdate (DD/MM/YYYY): ").strip()
    try:
        bday = datetime.strptime(s, "%d/%m/%Y").date()
        break
    except ValueError:
        print("Invalid format. Please use DD/MM/YYYY, e.g. 16/06/1994.")
```
Other nice tweaks:
- If `candles == 0`, show **10 candles** instead (`candles = 10`) so a multiple-of-10 birthday still looks festive.
- Print the computed **age** explicitly before the cake (`print("Age:", age)`).
- Internationalize: accept `DD-MM-YYYY` too, or auto-detect separators.

## Files
- `happy_birthday.py` — the script
- `README.md` — this file
