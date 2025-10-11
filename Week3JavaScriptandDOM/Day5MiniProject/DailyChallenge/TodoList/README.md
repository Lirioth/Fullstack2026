
# Daily Challenge — Todo List

**Last Updated:** October 7th, 2025

## What you will learn
- DOM events
- DOM tree

## Implemented
- HTML: form with one `input[type="text"]` and a **Submit** button.
- Below it, an empty `<div class="listTasks"></div>` container.
- JS:
  - `const tasks = []` as the data store (objects: `{ task_id, text, done }`).
  - `addTask()` validates, pushes to the array, and renders.
  - Each task has an **X** delete button (Font Awesome) and a **checkbox** with the task label.
  - `doneTask()` toggles the `done` property and updates styling.
  - `deleteTask()` removes the item from the array and DOM.
- CSS: simple, readable layout; `.done` shows strikethrough red text.

## Run
Open `index.html` in a browser.
