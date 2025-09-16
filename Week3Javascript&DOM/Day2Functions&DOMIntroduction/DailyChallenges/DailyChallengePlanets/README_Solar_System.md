# Mini‑Project — Solar System (Planets & Moons)

A tiny DOM project that renders a list of planets with colored circles and small orbiting moons.

---

## Files
- `planets.html` — minimal HTML + CSS for planets/moons layout (circle styling, absolute moons).  
- `planets.js` — data + DOM creation and simple orbit placement.

## How to run
1. Put `planets.html` and `planets.js` in the same folder.
2. Open `planets.html` in your browser.

> No build tools or frameworks required.

---

## How it works
- A `<section class="listPlanets">` acts as the container. JS selects it and applies a simple flex layout with wrapping and a gap.  
- An array of planet objects holds `name`, `color`, and `moons`. JS loops the array and, for each planet:
  - Creates a `.planet` div, sets its background color, writes the name, and appends it.
  - Creates `moons` number of `.moon` divs and places them around the planet using a rotate/translate trick:
    - angle = `(i / moons) * 360`
    - radius = `70px`
    - `transform: rotate(angle) translate(radius) rotate(-angle)` keeps each moon facing outward.

This yields a simple “orbit ring” effect without complex math.

---

## Customization
- **Colors:** edit the `color` hex per planet in the `planets` array.
- **Moons count:** change the `moons` integer. (Counts are demo values, not astronomical.)
- **Orbit radius:** tweak `r = 70` in JS.
- **Sizes:** adjust `.planet` / `.moon` `width/height` in CSS.
- **Spacing:** tune the container flex `gap`, and borders/typography as desired.

---

## Possible extensions
- Add hover tooltips with planet facts.
- Animate moons with CSS `@keyframes` rotation.
- Toggle moon visibility or change counts via a simple form.

---

## Accessibility & notes
- Ensure sufficient color contrast for planet labels.
- Prefer meaningful text or `aria-label` for screen readers.
- Keep in mind this is a **visual demo**; the moon counts/spacing are illustrative.
