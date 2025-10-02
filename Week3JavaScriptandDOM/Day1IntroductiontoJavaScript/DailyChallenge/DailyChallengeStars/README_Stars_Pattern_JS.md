# Daily Challenge — Stars Pattern (JavaScript)

Print the triangle pattern using **one loop** and using **two nested loops**.

```
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
```

---

## Files
- `index.html` — minimal UI with two buttons (one loop / two loops).
- `script.js` — functions: `oneLoop()` and `twoLoops()`.

## How to run
Open `index.html` in your browser and click **One loop** or **Two nested loops**.  
The pattern appears in the `<pre id="out">` block and is also logged to the console.

## How it works

### One loop (growing line)
- Keep a `line` string that grows by `"* "` each iteration.
- Push the current line (trimmed) to the output.

Pseudo-code:
```js
let rows = 6, line = "", out = "";
for (let i = 1; i <= rows; i++) {
  line += "* ";
  out += line.trim() + "\n";
}
```

### Two nested loops
- Outer loop controls the number of lines.
- Inner loop appends one `"* "` per column up to the current line index.

Pseudo-code:
```js
let rows = 6, out = "";
for (let i = 1; i <= rows; i++) {
  let line = "";
  for (let j = 1; j <= i; j++) line += "* ";
  out += line.trim() + "\n";
}
```

## Complexity
- Time: **O(n²)** (total stars printed is 1+2+…+n).
- Space: **O(n²)** to hold the full text in memory before printing.

## Optional enhancements
- Add an `<input type="number">` to let the user choose the number of rows.
- Use `Array.from({length: i}, () => "*").join(" ")` (nested-loop version) or `"* ".repeat(i)` (ES6+).
- Add a “Copy output” button (`navigator.clipboard.writeText(out)`).

## Testing checklist
- Default 6 rows prints exactly the triangle above.
- Changing rows (if added) updates both implementations identically.
- No trailing spaces at the end of each line thanks to `.trim()`.
