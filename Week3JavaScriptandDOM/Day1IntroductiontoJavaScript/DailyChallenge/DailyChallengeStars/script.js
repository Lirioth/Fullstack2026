function oneLoop() {
  var rows = 6; // number of lines
  var line = ""; // will grow each step
  var out = "";

  for (var i = 1; i <= rows; i++) {
    line += "* "; // add one star each time
    out += line.trim() + "\n";
  }

  document.getElementById("out").textContent = out;
  console.log("One loop:\n" + out);
}

function twoLoops() {
  var rows = 6;
  var out = "";

  for (var i = 1; i <= rows; i++) {
    // outer loop = lines
    var line = "";
    for (var j = 1; j <= i; j++) {
      // inner loop = stars per line
      line += "* ";
    }
    out += line.trim() + "\n";
  }

  document.getElementById("out").textContent = out;
  console.log("Two loops:\n" + out);
}
