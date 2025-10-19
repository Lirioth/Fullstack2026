# Daily Challenge — HTML Form (with JSON output)

Practice HTTP & forms basics by capturing form data and appending it to the DOM as a JSON string. No hearts are used; other emojis help highlight sections.

## What you will learn
- Basic HTML form structure (`label`, `input`, `button`)
- Listening to the `submit` event and preventing full-page reloads
- Reading values with `FormData` → `Object.fromEntries`
- Converting data to JSON with `JSON.stringify`
- Updating the DOM programmatically

## How it works
1. Fill in **Name** and **Last name**.
2. Click **Send**.
3. A JSON string is appended to the page (and a pretty-printed version is shown for readability).

## Project structure
```
daily-challenge-html-form/
├─ index.html        # The form and output area
├─ css/
│  └─ styles.css     # Minimal styling
└─ js/
   └─ app.js         # Logic with comments
```

## Run it
- Open `index.html` in your browser.
- Submit a few times and watch the list grow.
- Use the **Clear Output** button to reset the list.

## Notes
- This is a purely client-side demo (no network requests).
- The log uses an ordered list and an `aria-live` region so updates are announced by assistive tech.
- The strict requirement was to append the **JSON string**; the pretty JSON block is included as an extra learning aid.
- Emojis are used for headings and cues, but no hearts are included.

## Next steps
- Validate inputs (e.g., required fields) and display inline messages.
- Persist submissions in `localStorage` and restore on load.
- Add a GET form variant that displays the same JSON by parsing `window.location.search`.
