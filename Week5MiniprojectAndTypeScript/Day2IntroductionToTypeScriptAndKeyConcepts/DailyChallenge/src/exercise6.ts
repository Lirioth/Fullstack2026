// 🌟 Exercise 6: Object Type Annotations
// What You Will Learn:
// - How to define the structure of an object using TypeScript's type annotations.
// - How to create and return an object with specific properties.

// Define the Object Structure
type Person = {
  name: string;
  age: number;
};

// Create the Function
function createPerson(name: string, age: number): Person {
  return {
    name: name,
    age: age
  };
}

// Test the Function
const person1 = createPerson("Alice", 25);
console.log(person1); // Output: { name: 'Alice', age: 25 }

const person2 = createPerson("Bob", 30);
console.log(person2); // Output: { name: 'Bob', age: 30 }

// Accessing object properties
console.log(`Person 1: ${person1.name}, ${person1.age} years old`);
console.log(`Person 2: ${person2.name}, ${person2.age} years old`);
