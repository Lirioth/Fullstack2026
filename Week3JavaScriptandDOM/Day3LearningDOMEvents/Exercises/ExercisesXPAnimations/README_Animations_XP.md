# Exercises XP — Animations (DOM + Timers)

Two small animations exercises implemented with **vanilla JS**. Code is short and commented in English.

## Files
- `index_timer.html` — Exercise 1 (Timer: Parts I–III)
- `timer.js` — logic for Exercise 1
- `index_move.html` — Exercise 2 (Move the box)
- `move.js` — logic for Exercise 2

## How to run
Open either HTML file in your browser:
- `index_timer.html` — shows the container + "Clear Interval" button.
  - **Part I**: after 2s, an `alert("Hello World")` appears.
  - **Part II**: after 2s, a `<p>Hello World</p>` is appended to the container.
  - **Part III**: every 2s, a new `<p>Hello World</p>` is added. The interval stops when:
    - You click **Clear Interval**, or
    - There are **5 paragraphs** inside the container.
- `index_move.html` — click **Click Me** to start the animation.
  - The red box moves **1px every millisecond** to the right until it reaches the edge.
  - Starting the animation again resets the box to the left and re-runs the movement.

## Notes
- Uses `setTimeout`, `setInterval`, and `clearInterval` exactly as required.
- No frameworks; pure DOM API.
