// Daily Challenge GOLD: Bubble Sort
// Last Updated: October 7th, 2025
//
// Topics: array methods, loops, nested loops
//
// Requirements covered:
// - Convert array to string using toString() and join() with different separators
// - Sort numbers in descending order using nested for-loops (no built-in sort)
// - Use a temporary variable to swap values
// - Add console.log at each step to understand what's happening

const numbers = [5,0,9,1,7,4,2,6,3,8];

// 1) Convert to string with toString()
const toStringResult = numbers.toString();
console.log("toString():", toStringResult);

// 2) Convert to string with join() using different separators
console.log("join('+'):", numbers.join('+'));
console.log("join(' '):", numbers.join(' '));
console.log("join(''):", numbers.join(''));

// 3) Bubble Sort (descending) using nested for-loops and a temp variable
/**
 * Bubble sort in descending order using nested for-loops.
 * Does NOT use Array.prototype.sort.
 * Returns a new array and logs intermediate steps.
 */
function bubbleSortDescending(input) {
  const arr = input.slice(); // work on a copy
  const n = arr.length;
  console.log("\nStarting Bubble Sort (descending)...");
  console.log("Initial:", arr.join(','));

  for (let pass = 0; pass < n - 1; pass++) {
    let swapped = false; // track if this pass made any swap

    console.log(`\nPass ${pass + 1} (before):`, arr.join(','));

    // Inner loop compares adjacent pairs
    for (let i = 0; i < n - 1 - pass; i++) {
      // If the left element is smaller than the right, swap (for descending order)
      if (arr[i] < arr[i + 1]) {
        const temp = arr[i];     // temporary variable for swap
        arr[i] = arr[i + 1];
        arr[i + 1] = temp;
        swapped = true;
        console.log(` swap at indices ${i} and ${i+1} ->`, arr.join(','));
      } else {
        console.log(` no swap for indices ${i} and ${i+1} ->`, arr.join(','));
      }
    }

    console.log(`Pass ${pass + 1} (after):`, arr.join(','));

    // Optimization: if no swaps, the array is already sorted
    if (!swapped) {
      console.log("No swaps in this pass; array is sorted early.");
      break;
    }
  }

  console.log("\nFinished. Result:", arr.join(','));
  return arr;
}

const sortedDesc = bubbleSortDescending(numbers);

// 4) Final output check
console.log("\nExpected: [9,8,7,6,5,4,3,2,1,0]");
console.log("Actual:   [" + sortedDesc.join(',') + "]");
