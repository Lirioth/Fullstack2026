# Exercises XP — Fetch API & Async/Await (separate files)

Learn and practice:
- Fetch API
- Async/Await
- Proper status checks and error handling

## Files
```
exercises-xp-fetch-async/
├─ index.html         # Buttons to run each exercise + output panel
├─ css/
│  └─ styles.css
└─ js/
   └─ app.js          # Implementations for Exercises 1–4
```

## Usage
1. Open `index.html` in a browser with internet access.
2. Open DevTools (Console).
3. Click each button to run the respective exercise:
   - Exercise 1: Giphy search for “hilarious” — logs full JSON to console and a summary to the panel.
   - Exercise 2: Giphy search for “sun” with `limit=10&offset=2` — logs full JSON and shows titles.
   - Exercise 3: SWAPI starship (async/await only) — logs `objectStarWars.result` to console and the name to the panel.
   - Exercise 4: Shows `calling` immediately, then after ~2 seconds `resolved`.

## Notes
- Uses the provided GIPHY API key from the prompt.
- All requests check `response.ok` and throw for non-2xx status codes, caught with `try/catch`.
- Panel shows a compact summary; the Console displays the full response objects.
- Emojis are used for clarity; no hearts.
