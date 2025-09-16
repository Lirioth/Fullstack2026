// Exercises XP Gold — JS (short & simple)
// Open index.html in a browser and watch the console (DevTools).
// Each exercise logs its results. Exercise 2 also shows an alert.

// -----------------------------
// Exercise 1 : Divisible by three
// -----------------------------
{
  // Given numbers
  const numbers = [123, 8409, 100053, 333333333, 7];
  console.log("Exercise 1: Divisible by 3?");
  // Loop and print true/false
  for (let i = 0; i < numbers.length; i++) {
    const n = numbers[i];
    console.log(n % 3 === 0); // true if divisible by 3, else false
  }
}

// -----------------------------
// Exercise 2 : Attendance
// -----------------------------
{
  // Key = name (lowercase), value = country
  const guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina",
  };

  console.log("\nExercise 2: Attendance");
  // Ask for the student's name (browser prompt)
  const input = prompt("What is your name? (randy, karla, wendy, norman, sam)");
  // Normalize to lowercase and trim spaces; handle cancel (null)
  const name = (input || "").trim().toLowerCase();

  // Use the 'in' operator as hinted by the exercise
  if (name && name in guestList) {
    const country = guestList[name];
    const msg = `Hi! I'm ${name}, and I'm from ${country}.`;
    console.log(msg);
    alert(msg); // small UX touch
  } else {
    const msg = "Hi! I'm a guest.";
    console.log(msg);
    if (input !== null) alert(msg);
  }
}

// -----------------------------
// Exercise 3 : Playing with numbers
// -----------------------------
{
  // Given ages
  const age = [20, 5, 12, 43, 98, 55];
  console.log("\nExercise 3: Playing with numbers");

  // 1) Sum of all numbers (no built-ins)
  let sum = 0;
  for (let i = 0; i < age.length; i++) {
    sum += age[i];
  }
  console.log("Sum:", sum);

  // 2) Highest age (no Math.max / no reduce)
  let max = age[0];                 // start with first element
  for (let i = 1; i < age.length; i++) {
    if (age[i] > max) max = age[i]; // update if a larger value is found
  }
  console.log("Highest age:", max);
}
