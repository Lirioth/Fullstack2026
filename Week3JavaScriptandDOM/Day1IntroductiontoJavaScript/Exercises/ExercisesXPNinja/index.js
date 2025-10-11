// 🗡️ Exercises XP Ninja — JS Basics
// Topics: Variables, Conditionals, Loops, Functions ✨
// Neutral tone; friendly emoji comments throughout.

// ----------------------------------------------------
// Exercise 1: Checking the BMI
// ----------------------------------------------------
// Two person objects. Each has a method to compute BMI (kg/m^2). 🧮
const personA = {
  fullName: "Alice Example",
  massKg: 68,
  heightM: 1.70,
  bmi() {
    return this.massKg / (this.heightM ** 2);
  },
};

const personB = {
  fullName: "Bob Sample",
  massKg: 85,
  heightM: 1.80,
  bmi() {
    return this.massKg / (this.heightM ** 2);
  },
};

/**
 * Compare the BMI of two people and report who has the larger BMI. 🥇
 * @param {{fullName:string,bmi:Function}} p1
 * @param {{fullName:string,bmi:Function}} p2
 * @returns {{winner:string|null, bmi1:number, bmi2:number, tie:boolean}}
 */
function compareBmi(p1, p2) {
  const bmi1 = Number(p1.bmi().toFixed(2));
  const bmi2 = Number(p2.bmi().toFixed(2));

  if (bmi1 > bmi2) {
    console.log(`🏆 ${p1.fullName} has the larger BMI: ${bmi1} vs ${bmi2}`);
    return { winner: p1.fullName, bmi1, bmi2, tie: false };
  } else if (bmi2 > bmi1) {
    console.log(`🏆 ${p2.fullName} has the larger BMI: ${bmi2} vs ${bmi1}`);
    return { winner: p2.fullName, bmi1, bmi2, tie: false };
  } else {
    console.log(`🤝 It's a tie! Both BMIs are ${bmi1}`);
    return { winner: null, bmi1, bmi2, tie: true };
  }
}

// ----------------------------------------------------
// Exercise 2: Grade Average
// ----------------------------------------------------

/**
 * Compute the average for a list of numeric grades. 📊
 * @param {number[]} gradesList
 * @returns {number} average (NaN if list is empty)
 */
function computeAverage(gradesList) {
  if (!Array.isArray(gradesList)) {
    throw new TypeError("gradesList must be an array of numbers");
  }
  if (gradesList.length === 0) return NaN;
  let sum = 0;
  for (let i = 0; i < gradesList.length; i++) { // 🔁 classic loop
    const g = Number(gradesList[i]);
    if (!Number.isFinite(g)) {
      throw new TypeError("All grades must be finite numbers");
    }
    sum += g;
  }
  return sum / gradesList.length;
}

/**
 * Print pass/fail message given an average. 🎓
 * Threshold is 65.
 * @param {number} avg
 */
function reportPassFail(avg) {
  if (!Number.isFinite(avg)) {
    console.log("⚠️ No grades to evaluate.");
    return;
  }
  if (avg > 65) {
    console.log(`✅ Passed with average: ${avg.toFixed(2)}`);
  } else if (avg < 65) {
    console.log(`❌ Failed with average: ${avg.toFixed(2)} — must repeat the course.`);
  } else {
    console.log(`🟨 Exactly 65 — borderline case.`);
  }
}

/**
 * As required by the exercise: a function named findAvg that
 * takes gradesList, logs the average, and prints pass/fail. 🧠
 * @param {number[]} gradesList
 */
function findAvg(gradesList) {
  const avg = computeAverage(gradesList);
  if (Number.isFinite(avg)) {
    console.log(`📏 Average: ${avg.toFixed(2)}`);
  }
  reportPassFail(avg);
  return avg;
}

// ----------------------------------------------------
// Demo / Manual run (Node): `node index.js`
// ----------------------------------------------------
if (require.main === module) {
  console.log("— Exercise 1 — BMI —");
  compareBmi(personA, personB);

  console.log("\n— Exercise 2 — Grades —");
  findAvg([80, 95, 70, 60, 88]);   // ✅ Pass example
  findAvg([40, 55, 60]);           // ❌ Fail example
}

// Export for testing if needed
module.exports = {
  personA,
  personB,
  compareBmi,
  computeAverage,
  reportPassFail,
  findAvg,
};
