// 🌟 Exercise 4: Control Flow with if...else
// What You Will Learn:
// - How to use if...else statements to control program flow.
// - How to handle different conditions using if...else statements.

function checkNumber(num: number): string {
  if (num > 0) {
    return "positive";
  } else if (num < 0) {
    return "negative";
  } else {
    return "zero";
  }
}

// Test the function
console.log(checkNumber(5));    // Output: positive
console.log(checkNumber(-3));   // Output: negative
console.log(checkNumber(0));    // Output: zero
console.log(checkNumber(100));  // Output: positive
console.log(checkNumber(-42));  // Output: negative
