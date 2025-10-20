// 🌟 Exercise 5: Tuple Types
// What You Will Learn:
// - How to use tuple types in TypeScript.
// - How to define functions that return multiple values of different types.

function getDetails(name: string, age: number): [string, number, string] {
  const greeting = `Hello, ${name}! You are ${age} years old.`;
  return [name, age, greeting];
}

// Call the function and log the tuple
const details = getDetails("Alice", 25);

// Expected output
console.log(details); // Output: ['Alice', 25, 'Hello, Alice! You are 25 years old.']

// Test with more examples
const details2 = getDetails("Bob", 30);
console.log(details2); // Output: ['Bob', 30, 'Hello, Bob! You are 30 years old.']

// Accessing individual tuple elements
console.log(`Name: ${details[0]}`);
console.log(`Age: ${details[1]}`);
console.log(`Greeting: ${details[2]}`);
