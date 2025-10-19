// Module: app
// Purpose: Import people (ESM) and compute average age.
// Author: Kevin "Lirioth" Cusnir
// Date: 2025-10-19 | TZ: Asia/Jerusalem
// Notes: Minimal logic, clear output ✅

import { people } from "./data.js";

/**
 * Compute the average age, guarded against empty lists.
 * @param {Array<{age:number}>} arr - List of items with `age` fields.
 * @returns {number} Average age rounded to 2 decimals.
 */
function averageAge(arr) {
  if (!Array.isArray(arr) || arr.length === 0) {
    console.log("⚠️  No data to compute average.");
    return 0;
  }
  const sum = arr.reduce((acc, p) => acc + Number(p.age || 0), 0);
  return Math.round((sum / arr.length) * 100) / 100;
}

const avg = averageAge(people);
console.log(`🧠 Average age across ${people.length} people: ${avg}`);
