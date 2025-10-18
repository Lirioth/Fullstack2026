// Exercise 2 — Move the box
// Use setInterval to move #animate 1px every millisecond until it reaches the right edge.

let moveId = null; // interval id (so we can avoid stacking intervals)

function myMove() {
  const box = document.getElementById("animate");
  const wrap = document.getElementById("container");

  // Clear any previous interval
  if (moveId !== null) {
    clearInterval(moveId);
    moveId = null;
  }

  // Start from left = 0
  let pos = 0;
  box.style.left = "0px";

  // Compute the last allowed left position (container width - box width)
  const limit = wrap.clientWidth - box.clientWidth;

  moveId = setInterval(() => {
    if (pos >= limit) {
      clearInterval(moveId);
      moveId = null;
      return;
    }
    pos += 1; // move 1px
    box.style.left = pos + "px";
  }, 1); // move every millisecond
}
