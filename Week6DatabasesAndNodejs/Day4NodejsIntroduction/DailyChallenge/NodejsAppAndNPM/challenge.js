// Module: challenge (integration)
// Purpose: Use greeting, colorful-message, and read-file together.

const { greet } = require("./greeting");
const { showColorfulMessage } = require("./colorful-message");
const { readAndPrint } = require("./read-file");

(async () => {
  console.log("🚀 Challenge — Integration Demo");
  console.log(greet("Developer"));
  showColorfulMessage();
  await readAndPrint();
  console.log("🎉 Challenge complete.");
})().catch(() => process.exit(1));
