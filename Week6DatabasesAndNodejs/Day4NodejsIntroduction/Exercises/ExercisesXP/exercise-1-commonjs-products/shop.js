// Module: shop
// Purpose: Import products (CommonJS) and provide a simple search by product name.
// Author: Kevin "Lirioth" Cusnir
// Date: 2025-10-19 | TZ: Asia/Jerusalem
// Notes: Friendly console output with emojis; zero external deps.

/**
 * @typedef {import('./products')} ProductArray
 */

const products = require("./products");

/**
 * Find a product by name (case-insensitive).
 * @param {string} name - Product name to search.
 * @returns {object|null} The matching product object or null.
 */
function findProductByName(name) {
  if (typeof name !== "string" || !name.trim()) {
    console.log("⚠️  Please provide a non-empty product name.");
    return null;
  }
  const needle = name.trim().toLowerCase();
  const hit = products.find(p => p.name.toLowerCase() === needle);
  return hit || null;
}

// Demo calls ✅
["Mechanical Keyboard", "USB-C Hub", "Unknown"].forEach(query => {
  const result = findProductByName(query);
  if (result) {
    console.log(`✅ Found: ${result.name} — $${result.price} [${result.category}]`);
  } else {
    console.log(`❌ Not found: ${query}`);
  }
});

module.exports = { findProductByName };
