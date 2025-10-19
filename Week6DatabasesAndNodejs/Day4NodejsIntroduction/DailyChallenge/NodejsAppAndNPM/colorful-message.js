// Module: colorful-message
// Purpose: Show a colorful terminal message using chalk (CommonJS).

const chalk = require("chalk");

/**
 * Print a cheerful message with styles.
 */
function showColorfulMessage() {
  const title = chalk.bgBlue.white.bold(" Daily Challenge ");
  const tip = chalk.yellow("💡 Tip:");
  const details = chalk.reset("Try editing the message styles for fun!");
  console.log(`${title} ${chalk.green("Running Task 2")} ✅`);
  console.log(`${tip} ${details}`);
}

module.exports = { showColorfulMessage };
