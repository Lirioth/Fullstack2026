// Module: app
// Purpose: Use custom math module + lodash helpers to do small calculations.
// Author: Kevin "Lirioth" Cusnir
// Date: 2025-10-19 | TZ: Asia/Jerusalem
// Notes: Run `npm install` before executing. ✅

const _ = require("lodash");
const { add, multiply } = require("./math");

const nums = [2, 2, 3, 3, 3, 6];

// Unique & sorted list with lodash
const uniqueSorted = _.sortBy(_.uniq(nums));

// Compute the sum and product of the unique set
const sum = uniqueSorted.reduce((acc, n) => add(acc, n), 0);
const product = uniqueSorted.reduce((acc, n) => multiply(acc, n), 1);

console.log(`🧠 Unique numbers: ${uniqueSorted.join(", ")}`);
console.log(`✅ Sum: ${sum}`);
console.log(`⚙️  Product: ${product}`);
