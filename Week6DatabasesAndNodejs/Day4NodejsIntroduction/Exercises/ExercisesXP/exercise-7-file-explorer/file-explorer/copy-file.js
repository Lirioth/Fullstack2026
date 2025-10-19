// Module: copy-file
// Purpose: Copy contents from source.txt to destination.txt using fs (CommonJS).
// Author: Kevin "Lirioth" Cusnir
// Date: 2025-10-19 | TZ: Asia/Jerusalem
// Notes: Uses promises API for clarity.

const fs = require("fs").promises;
const path = require("path");

async function main() {
  const src = path.resolve(__dirname, "source.txt");
  const dst = path.resolve(__dirname, "destination.txt");

  try {
    const content = await fs.readFile(src, "utf-8");
    await fs.writeFile(dst, content, "utf-8");
    console.log(`✅ Copied content from ${path.basename(src)} to ${path.basename(dst)}`);
  } catch (err) {
    console.error(`❌ Copy failed: ${err.message}`);
    process.exit(1);
  }
}

main();
