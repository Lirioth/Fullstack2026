// 🌟 Exercise 9: Function Overloading with Default Parameters
// What You Will Learn:
// - How to use function overloading in TypeScript.
// - How to create overloaded functions with default parameters.

// Function overload signatures
function greet(name: string): string;
function greet(): string;

// Function implementation
function greet(name?: string): string {
  if (name) {
    return `Hello, ${name}!`;
  } else {
    return "Hello, there!";
  }
}

// Test the overloaded function
console.log(greet("Alice"));  // Output: Hello, Alice!
console.log(greet());         // Output: Hello, there!

// Additional examples
console.log(greet("Bob"));    // Output: Hello, Bob!
console.log(greet("Charlie"));// Output: Hello, Charlie!
console.log(greet());         // Output: Hello, there!

// More complex overloading example
function formatValue(value: number): string;
function formatValue(value: string): string;
function formatValue(value: boolean): string;

function formatValue(value: number | string | boolean): string {
  if (typeof value === "number") {
    return `Number: ${value}`;
  } else if (typeof value === "string") {
    return `String: "${value}"`;
  } else {
    return `Boolean: ${value}`;
  }
}

console.log(formatValue(42));      // Output: Number: 42
console.log(formatValue("hello")); // Output: String: "hello"
console.log(formatValue(true));    // Output: Boolean: true
