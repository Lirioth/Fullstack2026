
# Arrays & Destructuring — Exercises XP Gold (TypeScript) 🥇🧩

Practice **array methods** and **destructuring** with focused analyses and clean one-liners.

## ✅ What’s inside
- 1️⃣ `map` analysis → output is `[2, 4, 6]`
- 2️⃣ `reduce` analysis → output is `[1, 2, 0, 1, 2, 3]`
- 3️⃣ Map callback index `i` → for 6 elements: `0..5`
- 4️⃣ Nested arrays:
   - Transform `[[1],[2],[3],[[[4]]],[[[5]]]]` → `[1,2,3,[4],[5]]`
   - Bonus one‑liner included
   - Join greetings + full sentence
   - Free the trapped number: `[3]`

## 📂 Files
- `ArraysDestructuringXPGold.ts` — all solutions with small demo output (guarded).

## ▶️ Run locally
```bash
# Using ts-node
npx ts-node ArraysDestructuringXPGold.ts

# Or compile to JS and run
npx tsc ArraysDestructuringXPGold.ts
node ArraysDestructuringXPGold.js
```

## 🧪 Expected snippets
```
Ex1 analyzeMapOutput: [ 2, 4, 6 ]
Ex2 analyzeReduceOutput: [ 1, 2, 0, 1, 2, 3 ]
Ex3 indicesObserved: [ 0, 1, 2, 3, 4, 5 ]
Ex4 arrayFlattened: [ 1, 2, 3, [ 4 ], [ 5 ] ]
Ex4 greetingJoined: [ 'Hello young grasshopper!', 'you are', 'learning fast!' ]
Ex4 greetingSentence: Hello young grasshopper! you are learning fast!
Ex4 freed: [ 3 ]
```
