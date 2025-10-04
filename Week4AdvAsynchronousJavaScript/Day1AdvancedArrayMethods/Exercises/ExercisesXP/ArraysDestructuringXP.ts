// Arrays & Destructuring — Exercises XP (TypeScript, Single File)
// ---------------------------------------------------------------
// Covers: array methods, destructuring, forEach/map/filter/reduce, spread, switch, etc.
// Exported values/functions allow import-based checks. A small demo is included (guarded).

// ==============
// Exercise 1 : Colors
// ==============
export const colors1 = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];

export function listColorChoices_basic(): string[] {
  const out: string[] = [];
  colors1.forEach((c, i) => {
    out.push(`${i + 1}# choice is ${c}.`);
  });
  return out;
}

export function hasViolet(arr: string[] = colors1): string {
  return arr.includes("Violet") ? "Yeah" : "No...";
}

// ==============
// Exercise 2 : Colors #2
// ==============
export const ordinal = ["th", "st", "nd", "rd"]; // 0->th, 1->st, 2->nd, 3->rd

export function listColorChoices_ordinal(): string[] {
  const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
  return colors.map((c, i) => {
    const n = i + 1;
    const suffix = n >= 1 && n <= 3 ? ordinal[n] : ordinal[0];
    return `${n}${suffix} choice is ${c}.`;
  });
}

// ==============
// Exercise 3 : Analyzing (spread with arrays/strings/holes)
// ==============
export function analyzeSpread() {
  const fruits = ["apple", "orange"];
  const vegetables = ["carrot", "potato"];
  const result = ["bread", ...vegetables, "chicken", ...fruits];
  const fromCountry = [..."USA"];
  const newArray = [...[, ,]] as any[]; // holes become `undefined` when spread

  return { result, fromCountry, newArray };
}

// ==============
// Exercise 4 : Employees
// ==============
export type UserRec = { firstName: string; lastName: string; role: string };

export const users: UserRec[] = [
  { firstName: "Bradley", lastName: "Bouley", role: "Full Stack Resident" },
  { firstName: "Chloe", lastName: "Alnaji", role: "Full Stack Resident" },
  { firstName: "Jonathan", lastName: "Baughn", role: "Enterprise Instructor" },
  { firstName: "Michael", lastName: "Herman", role: "Lead Instructor" },
  { firstName: "Robert", lastName: "Hajek", role: "Full Stack Resident" },
  { firstName: "Wes", lastName: "Reid", role: "Instructor" },
  { firstName: "Zach", lastName: "Klabunde", role: "Instructor" },
];

export const welcomeStudents: string[] = users.map(u => `Hello ${u.firstName}`);

export const fullStackResidents: UserRec[] = users.filter(u => u.role === "Full Stack Resident");

export const lastNamesOfFSR: string[] = users
  .filter(u => u.role === "Full Stack Resident")
  .map(u => u.lastName);

// ==============
// Exercise 5 : Star Wars (reduce to string)
// ==============
export const epic = ["a", "long", "time", "ago", "in a", "galaxy", "far far", "away"];

export const epicSentence: string = epic.reduce((acc, cur, i) => (i === 0 ? cur : acc + " " + cur), "");

// ==============
// Exercise 6 : Employees #2
// ==============
export type Student = { name: string; course: string; isPassed: boolean };

export const students: Student[] = [
  { name: "Ray", course: "Computer Science", isPassed: true },
  { name: "Liam", course: "Computer Science", isPassed: false },
  { name: "Jenner", course: "Information Technology", isPassed: true },
  { name: "Marco", course: "Robotics", isPassed: true },
  { name: "Kimberly", course: "Artificial Intelligence", isPassed: false },
  { name: "Jamie", course: "Big Data", isPassed: false },
];

export const passedStudents: Student[] = students.filter(s => s.isPassed);

export function congratulatePassed(): string[] {
  const msgs: string[] = [];
  students
    .filter(s => s.isPassed)
    .forEach(s => msgs.push(`Good job ${s.name}, you passed the course in ${s.course}`));
  return msgs;
}

// ------------------------
// Optional demo (guarded):
// ------------------------
declare const require: any | undefined;
declare const module: any | undefined;

if (typeof require !== "undefined" && typeof module !== "undefined" && require.main === module) {
  console.log("Ex1 list:", listColorChoices_basic());
  console.log("Ex1 has Violet:", hasViolet());

  console.log("Ex2 list:", listColorChoices_ordinal());

  const { result, fromCountry, newArray } = analyzeSpread();
  console.log("Ex3 result:", result);          // ['bread','carrot','potato','chicken','apple','orange']
  console.log("Ex3 fromCountry:", fromCountry); // ['U','S','A']
  console.log("Ex3 newArray:", newArray);       // [undefined, undefined]

  console.log("Ex4 welcome:", welcomeStudents);
  console.log("Ex4 FSR only:", fullStackResidents.map(u => `${u.firstName} ${u.lastName}`));
  console.log("Ex4 FSR last names:", lastNamesOfFSR);

  console.log("Ex5 epic:", epicSentence); // "a long time ago in a galaxy far far away"

  console.log("Ex6 passed:", passedStudents.map(s => s.name));
  congratulatePassed().forEach(m => console.log(m));
}
