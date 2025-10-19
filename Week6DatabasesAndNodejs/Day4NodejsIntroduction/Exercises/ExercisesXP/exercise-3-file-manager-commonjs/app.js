// Module: app
// Purpose: Demo readFile + writeFile by copying text across two files.
// Author: Kevin "Lirioth" Cusnir
// Date: 2025-10-19 | TZ: Asia/Jerusalem
// Notes: Read 'Hello World.txt', then write to 'Bye World.txt'. ✅

const { readFile, writeFile } = require("./fileManager");

async function main() {
  const hello = await readFile("./Hello World.txt");
  console.log(`💡 Content of 'Hello World.txt': ${hello.trim()}`);
  await writeFile("./Bye World.txt", "Writing to the file");
  console.log("⚙️  Done.");
}

main().catch(() => process.exit(1));
