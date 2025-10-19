// Module: read-file
// Purpose: Read and print the content of files/file-data.txt (CommonJS).

const fs = require("fs").promises;
const path = require("path");

/**
 * Read and print file content.
 * @param {string} [relativePath] - Optional relative path to read (defaults to ./files/file-data.txt)
 * @returns {Promise<void>}
 */
async function readAndPrint(relativePath = "./files/file-data.txt") {
  const filePath = path.resolve(__dirname, relativePath);
  try {
    const data = await fs.readFile(filePath, "utf-8");
    console.log("📄 File content:");
    console.log(data);
    console.log("✅ Done.");
  } catch (err) {
    console.error(`❌ Failed to read: ${filePath} — ${err.message}`);
    throw err;
  }
}

module.exports = { readAndPrint };
