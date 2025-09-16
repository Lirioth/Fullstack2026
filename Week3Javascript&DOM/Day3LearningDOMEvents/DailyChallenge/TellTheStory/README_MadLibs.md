# Daily Challenge — Tell the story (Mad Libs)

A tiny DOM + Forms project: read five inputs (noun, adjective, name, verb, place) and generate a **Mad Libs** story. Includes a **Shuffle** button to remix the story using the same inputs.

## Files
- `index.html` — minimal form & output area (accessible, keyboard-friendly).
- `madlibs.js` — short, commented logic (submit, validate, render, shuffle).

## How to run
1. Put both files in the same folder.
2. Open `index.html` in your browser.
3. Fill all inputs and click **Lib it!** to generate a story.
4. Click **Shuffle story** to cycle through different story templates (keeps your words).
5. Use **Reset** to clear the form and output.

## How it works
- On submit, we `preventDefault()`, **read & trim** values, and validate that none is empty.
- We build a story using one of several small **template functions** (ES6 template strings).
- The **Shuffle** button selects a *different* template when possible, keeping the same words.
- The story text is written to `#story` and announced via `aria-live="polite"`.

## Notes
- Errors are simple `alert(...)` prompts, and focus returns to the missing field.
- Add or tweak templates by editing the `templates` array in `madlibs.js`.
- Everything is vanilla JS—no dependencies.
