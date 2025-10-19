// Module: read-directory
// Purpose: Read and print file list of current directory using fs (CommonJS).
// Author: Kevin "Lirioth" Cusnir
// Date: 2025-10-19 | TZ: Asia/Jerusalem
// Notes: Keep output simple and readable.

const fs = require("fs").promises;
const path = require("path");

async function main() {
  try {
    const here = __dirname;
    const files = await fs.readdir(here);
    console.log(`🧠 Files in ${path.basename(here)}:`);
    files.forEach(name => console.log(`- ${name}`));
  } catch (err) {
    console.error(`❌ Failed to read directory: ${err.message}`);
    process.exit(1);
  }
}

main();
