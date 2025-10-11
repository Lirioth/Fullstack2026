# Daily Challenge — Todo List

**Last Updated:** October 7th, 2025

## ✅ What you will learn
- DOM events 🖱️
- DOM tree 🌲

---

## 📋 Requirements implemented
- HTML: a form with one `input[type="text"]` and a **Submit** button.
- An empty `<div class="listTasks"></div>` below the form.
- JS:
  - `const tasks = []` (array of tasks).
  - `addTask()` validates non-empty input, pushes to the array, and renders below the form.
  - Each task row has:
    - an **“X”** delete button (Font Awesome) ❌
    - a **checkbox** ✅ with its label showing the task text.
- **BONUS I**: tasks are **objects** `{ task_id, text, done }`, with `data-task-id` on the DOM element. `doneTask()` toggles the `done` property and styles (red + strikethrough).
- **BONUS II**: `deleteTask()` removes the task from both the array and the DOM.

---

## ▶️ Run
Open `index.html` in a browser.  
Type a task → **Submit** → task appears with a checkbox and an X button.

---

## 🗂️ Files
- `index.html`
- `styles.css`
- `script.js`
