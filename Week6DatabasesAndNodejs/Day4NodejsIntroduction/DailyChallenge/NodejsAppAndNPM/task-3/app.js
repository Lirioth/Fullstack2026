// Module: app (Task 3)
// Purpose: Use the read-file module to display content.

const { readAndPrint } = require("../read-file");

console.log("🧪 Task 3 — Advanced File Operations");
readAndPrint().catch(() => process.exit(1));
