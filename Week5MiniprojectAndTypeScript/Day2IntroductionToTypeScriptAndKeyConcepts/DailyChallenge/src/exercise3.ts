// 🌟 Exercise 3: Union Types
// What You Will Learn:
// - How to use union types in TypeScript.
// - How to define variables that can hold either a string or a number.

let id: string | number;

// id can be a string
id = "ABC123";
console.log(`ID as string: ${id}`);

// id can also be a number
id = 12345;
console.log(`ID as number: ${id}`);

// Function demonstrating union type usage
function displayId(id: string | number): void {
  console.log(`The ID is: ${id}`);
}

displayId("XYZ789");
displayId(98765);
