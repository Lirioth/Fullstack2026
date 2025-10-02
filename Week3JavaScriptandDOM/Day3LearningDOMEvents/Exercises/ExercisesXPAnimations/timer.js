// Exercise 1 — Timer
// Short & simple, with English comments.

// Part I: after 2 seconds, alert "Hello World"
setTimeout(() => {
  alert("Hello World");
}, 2000);

// Part II: after 2 seconds, add <p>Hello World</p> inside #container
setTimeout(() => {
  const container = document.getElementById("container");
  const p = document.createElement("p");
  p.textContent = "Hello World";
  container.appendChild(p);
}, 2000);

// Part III: every 2 seconds, add <p>Hello World</p>; stop on button click OR when 5 paragraphs exist
const container = document.getElementById("container");
const clearBtn = document.getElementById("clear");

let addInterval = setInterval(() => {
  const p = document.createElement("p");
  p.textContent = "Hello World";
  container.appendChild(p);

  // If there are 5 paragraphs, clear the interval
  const count = container.querySelectorAll("p").length;
  if (count >= 5) {
    clearInterval(addInterval);
    addInterval = null;
  }
}, 2000);

clearBtn.addEventListener("click", () => {
  if (addInterval !== null) {
    clearInterval(addInterval);
    addInterval = null;
  }
});
