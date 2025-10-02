# Exercises XP Gold — JavaScript (Short & Simple)

Three small JS exercises using **variables**, **conditionals**, **loops**, and **objects**.  
Code is intentionally short and commented in English for clarity.

---

## Files
- `index.html` — minimal runner (loads `script.js`, shows a prompt for Exercise 2).
- `script.js` — solutions for the three exercises.

## How to run
1. Open `index.html` in your **browser**.
2. Open DevTools → **Console** to see the output.
3. Exercise 2 will show a `prompt(...)` asking for a name.

> Note: The `prompt()` API is only available in browsers (not in Node).

---

## What’s inside

### Exercise 1 — Divisible by three
- Given: `let numbers = [123, 8409, 100053, 333333333, 7]`  
- Loop through the array and `console.log(true/false)` depending on `n % 3 === 0`.

### Exercise 2 — Attendance
- Given a `guestList` object mapping **name → country**.
- Ask the user for a name with `prompt`.
- If the lowercased name is in the object → log/alert: `Hi! I'm [name], and I'm from [country].`
- Else → log/alert: `Hi! I'm a guest.`

### Exercise 3 — Playing with numbers (no built-in helpers)
- Given: `let age = [20,5,12,43,98,55];`
- Sum all numbers using a simple `for` loop.
- Find the **highest** number using a simple `for` loop (no `Math.max`, no `reduce`).

---

## Example output (one run)
```
Exercise 1: Divisible by 3?
true
true
true
true
false

Exercise 2: Attendance
(Shows a prompt, then prints one of the two messages)

Exercise 3: Playing with numbers
Sum: 233
Highest age: 98
```

## Notes
- Input for Exercise 2 is matched **case-insensitively** by lowercasing.
- Canceling the prompt prints the guest message in the console (no alert).
