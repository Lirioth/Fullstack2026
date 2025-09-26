# Daily Challenge — Groceries

Short, commented solution that demonstrates **pass-by-value** (primitives) vs **pass-by-reference** (objects) using the provided `client` and `groceries` data.

## Files
- `index.html` — minimal UI with buttons to run the functions and a note to check the console.
- `groceries.js` — solution code with clear console logs and comments.

## How to run
1. Put both files in the same folder.
2. Open `index.html` in your browser.
3. Open DevTools → **Console** to see the outputs.
4. Click the buttons to call `displayGroceries()` and `cloneGroceries()`.

## What’s implemented
- `displayGroceries`: logs each fruit via `forEach`.
- `cloneGroceries`:
  - Copies `client` into `user` (**value copy**) and shows that changing `client` does not change `user`.
  - Assigns `groceries` into `shopping` (**reference**) and shows mutations are visible from both.
  - Bonus: demonstrates a **deep clone** using `structuredClone` so mutations don’t leak.

## Notes
- `structuredClone` is supported in modern browsers; if needed, replace with `JSON.parse(JSON.stringify(groceries))` (no functions / Dates).
