"""
Challenges 2 - Code Analysis Module
====================================
Detailed analysis of sorting algorithm code.
Provides annotated version with comments and step-by-step execution trace.
Demonstrates selection sort algorithm understanding.

Author: Kevin Cusnir 'Lirioth'
Repository: Fullstack2026
Week 1 Day 5 - Mini Project
Python Version: 3.8+
"""

ANNOTATED = """
my_list = [2, 24, 12, 354, 233]                 # initial list
for i in range(len(my_list) - 1):               # outer loop: i = 0..3 (index of current position to fix)
    minimum = i                                  # assume the smallest so far is at position i
    for j in range(i + 1, len(my_list)):         # inner loop scans the remaining items (i+1 .. end)
        if (my_list[j] < my_list[minimum]):      # found a smaller value at index j?
            minimum = j                           # update 'minimum' to the new smallest index so far
            if (minimum != i):                    # if the smaller value is not already at position i
                # swap immediately to place the current smallest at i
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
print(my_list)                                   # final list (sorted ascending)
"""

def selection_like_sort_with_trace(a):
    """Perform the selection-like sort shown above and yield a trace of steps."""
    arr = a[:]  # work on a copy
    steps = []
    steps.append((None, None, None, arr[:], "init"))
    for i in range(len(arr) - 1):
        minimum = i
        for j in range(i + 1, len(arr)):
            # Comparison step
            if arr[j] < arr[minimum]:
                minimum = j
                if minimum != i:
                    # swap immediately
                    arr[i], arr[minimum] = arr[minimum], arr[i]
                    steps.append((i, j, minimum, arr[:], "swap"))
            else:
                steps.append((i, j, minimum, arr[:], "check"))
    return arr, steps

def pretty_trace(steps):
    """Format the trace for readable printing."""
    lines = []
    lines.append("Trace columns: i, j, minimum, list_snapshot, event")
    for (i, j, minimum, snapshot, event) in steps:
        lines.append(f"i={i}, j={j}, min_idx={minimum}, list={snapshot}, event={event}")
    return "\n".join(lines)

if __name__ == "__main__":
    data = [2, 24, 12, 354, 233]
    final_list, steps = selection_like_sort_with_trace(data)
    print("=== Annotated Code ===\n" + ANNOTATED)
    print("=== Step-by-step Trace ===")
    print(pretty_trace(steps))
    print("\nFinal Output:", final_list)
