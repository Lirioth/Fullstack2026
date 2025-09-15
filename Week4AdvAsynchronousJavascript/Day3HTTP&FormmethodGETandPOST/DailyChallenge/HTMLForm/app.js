// My goal: read two inputs and print a JSON string on the page

// 1) Grab the elements from the DOM
const form = document.getElementById('userForm');
const firstInput = document.getElementById('firstName');
const lastInput = document.getElementById('lastName');
const output = document.getElementById('output');
const historyList = document.getElementById('history');

// 2) Listen for the submit event
form.addEventListener('submit', function handleSubmit(event) {
  event.preventDefault(); // stop the page from reloading

  // 3) Read and clean the values
  const first = firstInput.value.trim();
  const last = lastInput.value.trim();

  // 4) Simple validation (very basic)
  if (!first || !last) {
    // show an error as JSON (so I keep everything in one style)
    output.textContent = JSON.stringify(
      { error: 'Please type both first and last name.' },
      null,
      2
    );
    return;
  }

  // 5) Build a tiny object with the data
  const data = {
    firstName: first,
    lastName: last
  };

  // 6) Convert the object to a JSON string (pretty with 2 spaces)
  const jsonText = JSON.stringify(data, null, 2);

  // 7) Print the JSON string into the <pre> element
  output.textContent = jsonText;

  // 8) Optional: add the JSON to a history list (so I can see previous submits)
  const li = document.createElement('li');
  li.textContent = jsonText;
  historyList.prepend(li);

  // 9) Optional: reset the form and focus the first field
  form.reset();
  firstInput.focus();
});

/*
  EXTRA NOTES (learning corner):

  - This file only shows how to read a form and print a JSON string on the DOM.
  - If I really wanted to SEND the data to a server, I could do:
      // POST example (send JSON to my server)
      fetch('/api/people', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ firstName: first, lastName: last })
      });

      // GET example (query string, not really used for sending form bodies):
      // /api/people?firstName=John&lastName=Doe

  - For this daily challenge the goal is to keep it simple and readable.
*/
