// Daily Challenge — HTML Form
// Requirements:
// - Build a form with name and last name fields + submit button
// - On Send, read the inputs and append a JSON string to the DOM
// - Use English comments and keep it clear; emojis are allowed (but no hearts)

/** Grab references to DOM elements we need */
const form = document.getElementById('userForm');
const log = document.getElementById('log');
const clearBtn = document.getElementById('clear');

/** Utility: create an element with text content and optional class */
function el(tag, text, className){
  const n = document.createElement(tag);
  if (text != null) n.textContent = text;
  if (className) n.className = className;
  return n;
}

/** Append one JSON entry to the log as a list item */
function appendJsonEntry(obj){
  const li = document.createElement('li');

  // Optional small timestamp (helps students see multiple submissions)
  const stamp = new Date().toLocaleTimeString();
  li.appendChild(el('div', 'Submitted at ' + stamp, 'timestamp'));

  // Show the JSON string (single line) and a pretty version under it
  const jsonStr = JSON.stringify(obj);
  const pre = document.createElement('pre');
  pre.textContent = jsonStr; // requirement: append the JSON string to the DOM
  li.appendChild(pre);

  // Also show a pretty-printed version for readability (educational bonus)
  const pretty = document.createElement('pre');
  pretty.textContent = JSON.stringify(obj, null, 2);
  pretty.setAttribute('aria-label', 'Pretty JSON');
  li.appendChild(pretty);

  log.appendChild(li);
}

/** Handle form submission: prevent navigation, collect values, append JSON */
form.addEventListener('submit', (e) => {
  e.preventDefault(); // avoid page reload

  // Gather values via FormData + Object.fromEntries
  const data = new FormData(form);
  const obj = Object.fromEntries(data.entries());

  // Ensure only the two required fields are present
  const payload = {
    name: obj.name ?? '',
    lastname: obj.lastname ?? ''
  };

  appendJsonEntry(payload);
});

/** Clear the output log (not required by the brief; convenient during testing) */
clearBtn.addEventListener('click', () => {
  log.innerHTML = '';
});
