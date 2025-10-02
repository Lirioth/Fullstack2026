# Exercises XP — DOM, Events & Forms

Short, commented JavaScript solutions for 4 DOM exercises. All sections are on a single page with minimal CSS.

## Files
- `index_dom_exercises.html` — structured HTML for the four exercises.
- `dom_exercises.js` — all the logic (event handlers, DOM manipulations).
- `README_DOM_XP.md` — this file.

## How to run
1. Put all files in the same folder.
2. Open `index_dom_exercises.html` in your browser.
3. Use DevTools → Console to see logs from Exercises 1–2.

## What’s implemented

### Exercise 1 — Change the article
- Logs the `<h1>` element.
- Removes the last `<p>` in the `<article>`.
- Click `<h2>` → background becomes red.
- Click `<h3>` → it hides (`display: none`).
- Button → makes **all paragraphs bold**.
- **Bonus:** Hover `<h1>` randomizes font size (0–100px) and resets on leave.
- **Bonus:** Hover the 2nd paragraph → CSS fade-out animation (then it resets).

### Exercise 2 — Work with forms
- Logs the form, inputs by **id** and by **name**.
- On submit (with `preventDefault()`): validates non-empty, creates two `<li>`s and appends to `.usersAnswer`.

### Exercise 3 — Transform the sentence
- `getBoldItems()` collects all `<strong>` elements in the paragraph.
- `highlight()` turns them **blue** on hover.
- `returnItemsToDefault()` resets them to **black** on mouse leave.

### Exercise 4 — Volume of a sphere
- On submit: reads radius, validates, then sets `volume` to `(4/3)*π*r^3` (fixed to 4 decimals).

## Notes
- Pure vanilla JS; no frameworks.
- Keep the console open to see informative logs.
