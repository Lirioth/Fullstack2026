// Arrays & Destructuring — Exercises XP Gold (TypeScript, Single File)
// -------------------------------------------------------------------
// Covers: array methods, destructuring, spread, flat/flatMap, map/filter/reduce, and analysis outputs.
// Exported values/functions allow import-based checks. A small demo is included (guarded).

// ==============
// Exercise 1 : Analyzing the map method
// ==============
// Code:
// [1, 2, 3].map(num => {
//   if (typeof num === 'number') return num * 2;
//   return;
// });
// Since every element is a number, each branch returns num*2; map preserves length.
// Output: [2, 4, 6]
export const analyzeMapOutput: number[] = [1, 2, 3].map(num => {
  if (typeof num === 'number') return num * 2;
  return undefined as unknown as number; // unreachable here, for typing
});

// ==============
// Exercise 2 : Analyzing the reduce method
// ==============
// Code:
// [[0, 1], [2, 3]].reduce(
//   (acc, cur) => {
//     return acc.concat(cur);
//   },
//   [1, 2],
// );
// Start with [1,2]; concat [0,1] then [2,3] => [1,2,0,1,2,3]
export const analyzeReduceOutput: number[] = [[0, 1], [2, 3]].reduce<number[]>(
  (acc, cur) => acc.concat(cur),
  [1, 2],
);

// ==============
// Exercise 3 : Analyze this code
// ==============
// Callback signature of map: (value, index, array). Here `i` is the index of the current element.
// For arrayNum length 6, `i` will be 0,1,2,3,4,5 in successive iterations.
export const arrayNum = [1, 2, 4, 5, 8, 9];
export const indicesObserved: number[] = arrayNum.map((num, i) => i);

// ==============
// Exercise 4 : Nested arrays
// ==============
export const arrayNested = [[1],[2],[3],[[[4]]],[[[5]]]];

// Two-step approach: flatten once, then flatten any remaining nested arrays by one more level where needed.
export const arrayFlattened: (number | number[])[] = arrayNested
  .flat(1)                                // [1,2,3,[[4]],[[5]]]
  .map(x => Array.isArray(x) ? x.flat(1) : x); // [1,2,3,[4],[5]]

// Bonus (one-liner achieving the same):
export const arrayFlattenedOneLine: (number | number[])[] = arrayNested.flat(1).map(x => Array.isArray(x) ? x.flat(1) : x);

// Greeting transformations
export const greeting = [["Hello", "young", "grasshopper!"], ["you", "are"], ["learning", "fast!"]];

// 1) To ["Hello young grasshopper!","you are","learning fast!"]
export const greetingJoined: string[] = greeting.map(words => words.join(" "));

// 2) To 'Hello young grasshopper! you are learning fast!'
export const greetingSentence: string = greetingJoined.join(" ");

// Trapped number
export const trapped = [[[[[[[[[[[[[[[[[[[[[[[[[[3]]]]]]]]]]]]]]]]]]]]]]]]]];
export const freed: number[] = trapped.flat(Infinity); // -> [3]

// ------------------------
// Optional demo (guarded):
// ------------------------
declare const require: any | undefined;
declare const module: any | undefined;

if (typeof require !== "undefined" && typeof module !== "undefined" && require.main === module) {
  console.log("Ex1 analyzeMapOutput:", analyzeMapOutput); // [2,4,6]
  console.log("Ex2 analyzeReduceOutput:", analyzeReduceOutput); // [1,2,0,1,2,3]
  console.log("Ex3 indicesObserved:", indicesObserved); // [0,1,2,3,4,5]
  console.log("Ex4 arrayFlattened:", arrayFlattened); // [1,2,3,[4],[5]]
  console.log("Ex4 arrayFlattenedOneLine:", arrayFlattenedOneLine);
  console.log("Ex4 greetingJoined:", greetingJoined);
  console.log("Ex4 greetingSentence:", greetingSentence);
  console.log("Ex4 freed:", freed); // [3]
}
