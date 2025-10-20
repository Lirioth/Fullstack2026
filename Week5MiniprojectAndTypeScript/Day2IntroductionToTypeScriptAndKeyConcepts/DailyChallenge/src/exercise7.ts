// 🌟 Exercise 7: Type Assertions
// What You Will Learn:
// - How to use type assertions in TypeScript to cast an element to a specific type.
// - How to access and manipulate properties of an HTML element after casting.

// Get an Element from the DOM
const inputElement = document.getElementById("userInput");

// Use Type Assertion to cast the element to HTMLInputElement
const typedInput = inputElement as HTMLInputElement;

// Access the Element's Properties
if (typedInput) {
  typedInput.value = "Hello from TypeScript!";
  console.log("Input value set to:", typedInput.value);
  
  // Additional example: adding an event listener
  typedInput.addEventListener("input", (event) => {
    const target = event.target as HTMLInputElement;
    console.log("Current input value:", target.value);
  });
}

// Alternative syntax using angle brackets (less common in .tsx files)
const anotherInput = <HTMLInputElement>document.getElementById("anotherInput");
if (anotherInput) {
  anotherInput.placeholder = "Type something...";
  console.log("Placeholder set for another input");
}

// Example with button
const button = document.getElementById("submitBtn") as HTMLButtonElement;
if (button) {
  button.addEventListener("click", () => {
    console.log("Button clicked!");
    if (typedInput) {
      alert(`You entered: ${typedInput.value}`);
    }
  });
}
