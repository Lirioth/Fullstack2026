# 🥇 Exercises XP Gold - Advanced Function Techniques# 🥈 XP Gold — Functions (Short & Simple)



Three challenging exercises covering age calculation, mathematical series, and statistical simulation with dice.This repo contains a tiny Python script solving **three function-based exercises**:



## 📊 Quick Stats1) **⏰ When will I retire?**  

   - Hard-coded today: **2025-09-16** (as the exercise requests).  

- **Difficulty**: 🥈 Intermediate     - `get_age(year, month, day)` returns whole years.  

- **Time Required**: 60-90 minutes     - `can_retire(gender, dob)` returns **✅ True** if: men **67+**, women **62+**.  

- **Exercises**: 3 advanced challenges     - Input format for DOB: `yyyy/mm/dd`.

- **Concepts**: Date calculations, series summation, random simulation, statistics  

- **Prerequisites**: ExercisesXP completed2) **🧮 Sum: X + XX + XXX + XXXX**  

   - `series_sum(x)` uses string repetition for clarity.

## 🎓 Learning Objectives

3) **🎲 Double Dice**  

- ✅ Work with date calculations using `datetime` module   - `throw_dice()` returns 1..6.  

- ✅ Implement age-based business logic   - `throw_until_doubles()` counts throws until both dice match.  

- ✅ Use string manipulation for mathematical patterns   - `main()` repeats **100** doubles → prints **Total** and **Average** (2 decimals).

- ✅ Apply random simulation and calculate statistics

- ✅ Validate user input and handle edge cases---



## 🚀 Quick Start## 🚀 How to run



```bash```bash

cd Exercises/ExercisesXPGoldpython3 xpgoldfunctions.py

python xpgoldfunctions.py```

```

- For deterministic tests in Exercise 3, you can uncomment `random.seed(0)`.

## 📋 Exercises

---

### 1️⃣ When Will I Retire? ⏰

Calculate age and retirement eligibility (men: 67, women: 62)## Example session (one possible run)



### 2️⃣ Series Sum 🧮```

Calculate X + XX + XXX + XXXX (e.g., 3 + 33 + 333 + 3333 = 3702)=== Exercise 1 ===

Gender (m/f): m

### 3️⃣ Double Dice 🎲  DOB (yyyy/mm/dd): 1960/05/03

Simulate rolling until doubles, calculate average over 100 trialsYou can retire.



## 🔧 Troubleshooting=== Exercise 2 ===

Enter a digit X: 3

| Issue | Solution |Result: 3702

|-------|----------|

| Date format error | Use 'yyyy/mm/dd' format |=== Exercise 3 ===

| Invalid gender | Use 'm' or 'f' only |Total throws: 314

| Inconsistent averages | Increase trial count for better accuracy |Average throws to reach doubles: 3.14

```

---

> Notes:

**Author**: Kevin Cusnir 'Lirioth'  > - The exercise asks to hard-code the current date; in real apps, you’d use `datetime.date.today()`.

**Repository**: [Fullstack2026](https://github.com/Lirioth/Fullstack2026)  > - Retirement ages used: men 67, women 62 (as stated in the prompt).

**Week 1 Day 4** - Functions - Exercises XP Gold
