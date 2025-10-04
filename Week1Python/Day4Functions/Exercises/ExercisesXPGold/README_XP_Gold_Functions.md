# 🥈 XP Gold — Functions (Short & Simple)

This repo contains a tiny Python script solving **three function-based exercises**:

1) **⏰ When will I retire?**  
   - Hard-coded today: **2025-09-16** (as the exercise requests).  
   - `get_age(year, month, day)` returns whole years.  
   - `can_retire(gender, dob)` returns **✅ True** if: men **67+**, women **62+**.  
   - Input format for DOB: `yyyy/mm/dd`.

2) **🧮 Sum: X + XX + XXX + XXXX**  
   - `series_sum(x)` uses string repetition for clarity.

3) **🎲 Double Dice**  
   - `throw_dice()` returns 1..6.  
   - `throw_until_doubles()` counts throws until both dice match.  
   - `main()` repeats **100** doubles → prints **Total** and **Average** (2 decimals).

---

## 🚀 How to run

```bash
python3 xpgoldfunctions.py
```

- For deterministic tests in Exercise 3, you can uncomment `random.seed(0)`.

---

## Example session (one possible run)

```
=== Exercise 1 ===
Gender (m/f): m
DOB (yyyy/mm/dd): 1960/05/03
You can retire.

=== Exercise 2 ===
Enter a digit X: 3
Result: 3702

=== Exercise 3 ===
Total throws: 314
Average throws to reach doubles: 3.14
```

> Notes:
> - The exercise asks to hard-code the current date; in real apps, you’d use `datetime.date.today()`.
> - Retirement ages used: men 67, women 62 (as stated in the prompt).
