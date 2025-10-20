// 🌟 Exercise 8: switch Statement with Complex Conditions
// What You Will Learn:
// - How to use a switch statement in TypeScript.
// - How to handle multiple conditions using complex cases in a switch statement.

function getAction(role: string): string {
  switch (role) {
    case "admin":
      return "Manage users and settings";
    case "editor":
      return "Edit content";
    case "viewer":
      return "View content";
    case "guest":
      return "Limited access";
    default:
      return "Invalid role";
  }
}

// Test the function with different roles
console.log(getAction("admin"));    // Output: Manage users and settings
console.log(getAction("editor"));   // Output: Edit content
console.log(getAction("viewer"));   // Output: View content
console.log(getAction("guest"));    // Output: Limited access
console.log(getAction("unknown"));  // Output: Invalid role
