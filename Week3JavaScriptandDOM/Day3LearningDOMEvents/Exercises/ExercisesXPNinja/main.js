// Exercises XP Ninja — DOM, Events, Forms
// Last Updated: 2025-10-07
//
// Contains:
// 1) Tip calculator (calculateTip) 🍽️
// 2) Email validation (with & without regex) 📧
// 3) Geolocation (navigator.geolocation) 📍

// ————————————————————————————————————————————————
// Exercise 1 — Tip Calculator 🍽️
// ————————————————————————————————————————————————
function calculateTip() {
  // Grab values from the DOM
  const billAmountEl = document.getElementById("billAmt");
  const serviceQualityEl = document.getElementById("serviceQual");
  const numOfPeopleEl = document.getElementById("numOfPeople");
  const totalTipEl = document.getElementById("totalTip");
  const tipEl = document.getElementById("tip");
  const eachEl = document.getElementById("each");

  const billAmount = parseFloat(billAmountEl.value);
  const serviceQuality = parseFloat(serviceQualityEl.value);
  let numberOfPeople = parseInt(numOfPeopleEl.value, 10);

  // 1) Guard: serviceQuality must be > 0 and bill must be provided
  if (!serviceQuality || !Number.isFinite(billAmount)) {
    alert("Please enter bill amount and select a service quality.");
    return;
  }

  // 2) Default people to 1 if empty or < 1; hide "each"
  if (!Number.isFinite(numberOfPeople) || numberOfPeople < 1) {
    numberOfPeople = 1;
    numOfPeopleEl.value = String(numberOfPeople);
    eachEl.style.display = "none";
  } else {
    // Show "each" only if more than one person
    eachEl.style.display = numberOfPeople > 1 ? "inline" : "none";
  }

  // 3) Compute total per person tip
  const total = (billAmount * serviceQuality) / numberOfPeople;
  tipEl.textContent = total.toFixed(2);

  // 4) Reveal the total block
  totalTipEl.style.display = "block";
}

// Hide the total by default (Second Part requirement)
document.addEventListener("DOMContentLoaded", () => {
  const totalTipEl = document.getElementById("totalTip");
  if (totalTipEl) totalTipEl.style.display = "none";

  // Wire the click to call calculateTip() via onclick
  const calcBtn = document.getElementById("calculate");
  if (calcBtn) {
    calcBtn.onclick = calculateTip; // hint wanted onclick specifically
  }
});

// ————————————————————————————————————————————————
// Exercise 2 — Email Validation 📧
// ————————————————————————————————————————————————
// No-regex validation: basic structural checks
function isValidEmailNoRegex(value) {
  const s = String(value).trim();
  // must contain exactly one '@'
  const atIdx = s.indexOf("@");
  if (atIdx <= 0 || atIdx !== s.lastIndexOf("@")) return false;

  const local = s.slice(0, atIdx);
  const domain = s.slice(atIdx + 1);

  // local and domain must be non-empty
  if (!local || !domain) return false;

  // domain must contain a '.' not at start or end
  const dotIdx = domain.indexOf(".");
  if (dotIdx <= 0 || dotIdx === domain.length - 1) return false;

  // basic allowed characters check (letters, digits, . _ - +)
  const allowed = /^[A-Za-z0-9._+-]+$/;
  if (!allowed.test(local)) return false;
  // domain: labels separated by '.', allowed letters/digits/hyphen, ends with 2+ letters
  const domainAllowed = /^[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;
  if (!domainAllowed.test(domain)) return false;

  return true;
}

// Regex validation (compact, pragmatic; not full RFC)
function isValidEmailRegex(value) {
  const s = String(value).trim();
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  return re.test(s);
}

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("emailForm");
  const input = document.getElementById("emailInput");
  const msg = document.getElementById("emailMsg");

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const method = new FormData(form).get("method") || "noregex";
    const value = input.value;

    const ok = method === "regex" ? isValidEmailRegex(value) : isValidEmailNoRegex(value);
    msg.textContent = ok ? "✅ Looks like a valid email." : "❌ Invalid email format.";
    msg.style.color = ok ? "green" : "crimson";
  });
});

// ————————————————————————————————————————————————
// Exercise 3 — Geolocation 📍
// ————————————————————————————————————————————————
function getGeolocation() {
  const out = document.getElementById("geoOut");
  if (!("geolocation" in navigator)) {
    out.textContent = "⚠️ Geolocation API not available in this browser.";
    return;
  }
  out.textContent = "⏳ Requesting location…";
  navigator.geolocation.getCurrentPosition(
    (pos) => {
      const { latitude, longitude } = pos.coords;
      out.textContent = `Latitude: ${latitude}\nLongitude: ${longitude}`;
    },
    (err) => {
      out.textContent = `❌ Error: ${err.message}`;
    },
    { enableHighAccuracy: true, timeout: 10000, maximumAge: 0 }
  );
}

document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("geoBtn");
  if (btn) btn.addEventListener("click", getGeolocation);
});
