# TypeScript Daily Challenge - Basic Concepts

## 📚 What You Will Learn

This daily challenge covers essential TypeScript concepts including:
- Basic TypeScript programs and type annotations
- Union types for flexible variable typing
- Control flow with if...else and switch statements
- Tuples and object type annotations
- Type assertions for DOM manipulation
- Function overloading with default parameters

## 🗂️ Project Structure

```
DailyChallenge/
├── src/
│   ├── exercise1.ts  - Hello, World! Program
│   ├── exercise2.ts  - Type Annotations
│   ├── exercise3.ts  - Union Types
│   ├── exercise4.ts  - Control Flow with if...else
│   ├── exercise5.ts  - Tuple Types
│   ├── exercise6.ts  - Object Type Annotations
│   ├── exercise7.ts  - Type Assertions (DOM)
│   ├── exercise8.ts  - Switch Statement
│   └── exercise9.ts  - Function Overloading
├── dist/             - Compiled JavaScript files (auto-generated)
├── index.html        - HTML page for Exercise 7
├── package.json
├── tsconfig.json
└── README.md
```

## 🚀 Getting Started

### Prerequisites

**⚠️ Node.js Required**: This project requires Node.js and npm to be installed.

#### Installing Node.js (if not already installed)

1. **Download Node.js**: Visit [nodejs.org](https://nodejs.org/)
2. **Choose version**: Download the **LTS (Long Term Support)** version (recommended)
3. **Run installer**: Follow the installation wizard
   - ✅ Check "Automatically install necessary tools" option
   - ✅ This will install Node.js, npm, and other required tools
4. **Verify installation**: After installation, restart your terminal and run:
   ```bash
   node --version
   npm --version
   ```
   You should see version numbers (e.g., `v20.x.x` and `10.x.x`)

### 1. Install Dependencies

Once Node.js is installed, install the required packages:

```bash
npm install
```

This will install TypeScript as a dev dependency.

### 2. Compile TypeScript Files

To compile all TypeScript files to JavaScript:

```bash
npm run build
```

This creates the `dist/` folder with compiled `.js` files.

## 📝 Running the Exercises

### Run Individual Exercises

Each exercise can be run separately using npm scripts:

```bash
# Exercise 1: Hello, World!
npm run ex1

# Exercise 2: Type Annotations
npm run ex2

# Exercise 3: Union Types
npm run ex3

# Exercise 4: Control Flow with if...else
npm run ex4

# Exercise 5: Tuple Types
npm run ex5

# Exercise 6: Object Type Annotations
npm run ex6

# Exercise 7: Type Assertions (See special instructions below)
npm run ex7

# Exercise 8: Switch Statement
npm run ex8

# Exercise 9: Function Overloading
npm run ex9
```

### Run All Exercises at Once

To compile and run all exercises (except Exercise 7):

```bash
npm run all
```

### Exercise 7 - Special Instructions

Exercise 7 demonstrates **Type Assertions** with DOM manipulation and requires a browser:

1. First, compile the TypeScript:
   ```bash
   npm run build
   ```

2. Open `index.html` in your web browser (double-click the file or use Live Server in VS Code)

3. Open the browser's Developer Console (F12) to see the output

4. Interact with the input fields and button to see TypeScript's type assertions in action

## 📖 Exercise Descriptions

### 🌟 Exercise 1: Hello, World! Program
Learn to create a simple TypeScript program that logs "Hello, World!" to the console.

### 🌟 Exercise 2: Type Annotations
Practice defining variables with explicit type annotations (`number`, `string`).

### 🌟 Exercise 3: Union Types
Use union types to create variables that can hold multiple types (e.g., `string | number`).

### 🌟 Exercise 4: Control Flow with if...else
Implement a function using `if...else` statements to determine if a number is positive, negative, or zero.

### 🌟 Exercise 5: Tuple Types
Create functions that return tuples - fixed-length arrays with specific types for each element.

### 🌟 Exercise 6: Object Type Annotations
Define object structures using TypeScript's type annotations and create functions that return typed objects.

### 🌟 Exercise 7: Type Assertions
Learn to cast DOM elements to specific types (e.g., `HTMLInputElement`) to safely access their properties.

**Expected Output (in browser console):**
- Input value automatically set
- Placeholder text added
- Event listeners responding to user input

### 🌟 Exercise 8: Switch Statement with Complex Conditions
Use switch statements to handle multiple conditions based on user roles.

**Expected Output:**
```
Manage users and settings
Edit content
View content
Limited access
Invalid role
```

### 🌟 Exercise 9: Function Overloading with Default Parameters
Create overloaded functions that can accept different parameter combinations.

**Expected Output:**
```
Hello, Alice!
Hello, there!
Number: 42
String: "hello"
Boolean: true
```

## 🔧 Configuration Files

### `tsconfig.json`
TypeScript compiler configuration:
- **target**: ES2020 (modern JavaScript)
- **module**: CommonJS (Node.js compatibility)
- **strict**: Enabled for type safety
- **outDir**: Compiled files go to `dist/`
- **rootDir**: Source files in `src/`

### `package.json`
Project dependencies and scripts:
- Includes TypeScript as a dev dependency
- Custom npm scripts for easy exercise execution

## 💡 Tips

1. **Type Safety**: Pay attention to TypeScript's type checking - it helps catch errors before runtime
2. **Compile Errors**: If you see compilation errors, check the terminal output for details
3. **Console Output**: Use `console.log()` to verify your results
4. **Experimentation**: Feel free to modify the exercises and experiment with different values
5. **VS Code**: Use VS Code's IntelliSense (Ctrl+Space) to explore available methods and properties

## 🐛 Troubleshooting

### npm is not recognized
**Error**: `npm: The term 'npm' is not recognized...`

**Solution**: Node.js is not installed or not in your PATH.
1. Install Node.js from [nodejs.org](https://nodejs.org/)
2. Restart your terminal/PowerShell
3. Verify: `node --version` and `npm --version`

### TypeScript not found
```bash
npm install
```

### Permission errors on Windows
Run PowerShell as Administrator or use:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Can't see Exercise 7 output
- Make sure you compiled first: `npm run build`
- Open `index.html` in a browser (not just in VS Code)
- Check the browser console (F12 → Console tab)

## 📤 Submission

Don't forget to:
1. Test all exercises
2. Commit your code
3. Push to GitHub

```bash
git add .
git commit -m "Completed TypeScript Daily Challenge"
git push origin main
```

## 🎯 Good Luck!

You've got this! These exercises will build a solid foundation in TypeScript fundamentals.

---

**Last Updated:** October 8th, 2025
