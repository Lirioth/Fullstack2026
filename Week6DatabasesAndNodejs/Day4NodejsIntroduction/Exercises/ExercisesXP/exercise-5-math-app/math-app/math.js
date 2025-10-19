// Module: math
// Purpose: Export simple math helpers (CommonJS).
// Author: Kevin "Lirioth" Cusnir
// Date: 2025-10-19 | TZ: Asia/Jerusalem
// Notes: Pure functions; easy to test.

/**
 * Add two numbers.
 * @param {number} a
 * @param {number} b
 * @returns {number}
 */
function add(a, b) {
  return Number(a) + Number(b);
}

/**
 * Multiply two numbers.
 * @param {number} a
 * @param {number} b
 * @returns {number}
 */
function multiply(a, b) {
  return Number(a) * Number(b);
}

module.exports = { add, multiply };
