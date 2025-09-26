# Fullstack 2026

This repository collects the hands-on materials for the Fullstack 2026 program. Each top-level folder corresponds to one themed week with daily challenges and mini-projects.

## Folder overview

- **Week1Python**: Gradual introduction to Python fundamentals. Includes daily folders with exercises on basic syntax, data structures (lists, dictionaries), functions, and a small capstone project.
- **Week2OOP**: Deep dive into Object-Oriented Programming with Python, covering classes, inheritance, encapsulation, polymorphism, and module organization.
- **Week3JavascriptandDOM**: Client-side JavaScript challenges focused on core language features, DOM manipulation, event handling, and advanced functions, plus a closing mini-project.
- **Week4AdvAsynchronousJavascript**: Materials centered on asynchronous JavaScript, including HTTP handling, forms, and additional patterns for working with promises.
- **Week5**: Introductory TypeScript activities, highlighted by the `day1.ts` example file.

## General execution guidelines

### Python scripts
1. Ensure **Python 3.10+** is installed.
2. Create and activate a virtual environment if required by the exercise:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies listed in `requirements.txt` (if present in the exercise folder):
   ```bash
   pip install -r requirements.txt
   ```
4. Run scripts from the exercise directory:
   ```bash
   python script_name.py
   ```

### HTML and JavaScript examples
1. Opening the `.html` file in a modern browser is usually sufficient.
2. For modules or relative paths, use an extension such as **Live Server** (VS Code) or start a simple server:
   ```bash
   python -m http.server 8000
   ```
3. Visit `http://localhost:8000` and navigate to the relevant file.

### TypeScript exercises
1. Install Node.js (LTS recommended) and optionally TypeScript globally:
   ```bash
   npm install -g typescript
   ```
2. Compile `.ts` files within the exercise folder:
   ```bash
   tsc file.ts
   ```
3. Execute the generated JavaScript with Node:
   ```bash
   node file.js
   ```
   Alternatively, run `npx ts-node file.ts` to compile and execute in one step.

These instructions are general; review each folder for additional specific requirements.
