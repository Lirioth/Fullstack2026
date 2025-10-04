"""
Demo runner for Challenges #2.
Prints the three required patterns and runs Exercise 2 analysis with a trace.
"""
from src.patterns import pattern_a, pattern_b, pattern_c
from src.ex2analysis import ANNOTATED, selection_like_sort_with_trace, pretty_trace

def main():
    print("=== Exercise 1: Patterns ===\n")
    print("-> Pattern A")
    pattern_a()
    print("\n-> Pattern B")
    pattern_b()
    print("\n-> Pattern C")
    pattern_c()

    print("\n=== Exercise 2: Analysis ===\n")
    print("Annotated code:")
    print(ANNOTATED)

    data = [2, 24, 12, 354, 233]
    final_list, steps = selection_like_sort_with_trace(data)
    print("Trace:")
    print(pretty_trace(steps))
    print("\nFinal Output:", final_list)

if __name__ == "__main__":
    main()
