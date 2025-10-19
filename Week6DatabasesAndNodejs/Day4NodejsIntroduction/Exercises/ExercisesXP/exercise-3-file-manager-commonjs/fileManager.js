// Module: fileManager
// Purpose: Provide readFile / writeFile using Node's fs module (Promise-based).
// Author: Kevin "Lirioth" Cusnir
// Date: 2025-10-19 | TZ: Asia/Jerusalem
// Notes: Uses UTF-8 by default; safe error messages.

const fs = require("fs").promises;
const path = require("path");

/**
 * Read a text file (UTF-8).
 * @param {string} filePath - Path to the file.
 * @returns {Promise<string>} File contents.
 */
async function readFile(filePath) {
  const abs = path.resolve(filePath);
  try {
    const data = await fs.readFile(abs, "utf-8");
    console.log(`✅ Read: ${abs}`);
    return data;
  } catch (err) {
    console.error(`❌ Failed to read ${abs} — ${err.message}`);
    throw err;
  }
}

/**
 * Write text to a file (UTF-8). Creates parent directories if needed.
 * @param {string} filePath - Path to the file.
 * @param {string} content - Text to write.
 * @returns {Promise<void>}
 */
async function writeFile(filePath, content) {
  const abs = path.resolve(filePath);
  try {
    await fs.mkdir(path.dirname(abs), { recursive: true });
    await fs.writeFile(abs, content, "utf-8");
    console.log(`✅ Wrote: ${abs}`);
  } catch (err) {
    console.error(`❌ Failed to write ${abs} — ${err.message}`);
    throw err;
  }
}

module.exports = { readFile, writeFile };
