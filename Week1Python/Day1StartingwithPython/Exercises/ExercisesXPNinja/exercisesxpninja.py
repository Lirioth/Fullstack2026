"""Module: exercisesxpninja
Purpose: Advanced Day 1 challenges exploring logic, text analysis, and constraints.
Author: Kevin Cusnir "Lirioth"
Created: 2025-10-18
Last Updated: 2025-10-19

Overview:
    1. Terminal concepts (PATH, aliases)
    2. Boolean logic edge cases and arithmetic
    3. String length analysis with Lorem Ipsum
    4. Character constraint challenges (no letter 'A')
"""

# 🎯 Constants
MAX_ATTEMPTS = 10  # ⚠️ Prevent infinite loops during the no 'A' challenge.


def exercise_1_2_terminal_concepts() -> None:
    """
    Display informational notes about terminal usage and Python execution.
    
    Covers:
    - Running Python from command line
    - PATH environment variable concept
    - Platform-specific Python launchers
    
    This is educational content, not interactive.
    """
    print("🥇 Exercise 1-2: Terminal Concepts")
    print("💡 INFO: Use 'python3' in terminal to run Python")
    print("💡 INFO: PATH is a list of directories searched for executables")
    print("💡 INFO: 'py' launcher (Windows) or alias (Linux/Mac)")


def exercise_3_boolean_outputs() -> None:
    """Demonstrate advanced boolean comparison behaviors and arithmetic."""
    print("\n🥇 Exercise 3: Boolean Outputs")
    print("🧪 Boolean Comparisons:")
    print(f"  3 <= 3 < 9: {3 <= 3 < 9}")  # True (chained)
    print(f"  3 == 3 == 3: {3 == 3 == 3}")  # True
    print(f"  bool(0): {bool(0)}")  # False
    print(f"  bool(5 == '5'): {bool(5 == '5')}")  # False
    print(f"  bool(4 == 4) == bool('4' == '4'): {bool(4 == 4) == bool('4' == '4')}")  # True
    print(f"  bool(bool(None)): {bool(bool(None))}")  # False
    
    # Boolean arithmetic (True=1, False=0)
    x = (1 == True)  # True
    y = (1 == False)  # False
    a = True + 4  # 5 (True behaves like 1)
    b = False + 10  # 10 (False behaves like 0)
    print(f"\n🔢 Boolean Arithmetic:")
    print(f"  x (1 == True): {x}")
    print(f"  y (1 == False): {y}")
    print(f"  a (True + 4): {a}")
    print(f"  b (False + 10): {b}")


def exercise_4_text_length() -> None:
    """
    Analyze length of a multi-line Lorem Ipsum text block.
    
    Demonstrates that len() counts ALL characters including:
    - Spaces
    - Newlines (\n)
    - Punctuation
    
    Example Output:
        📏 Text length (including spaces/newlines): 452
    """
    my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco 
laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit 
esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, 
sunt in culpa qui officia deserunt mollit anim id est laborum."""
    print(f"📏 Text length (including spaces/newlines): {len(my_text)}")


def exercise_5_no_a_challenge() -> None:
    """
    Challenge user to type sentences without letter 'A' with attempt limit.
    
    Features:
    - Case-insensitive 'A' detection
    - Maximum attempt limit (prevents infinite loops)
    - Best sentence tracking
    - Statistics display
    
    Rules:
    - Type sentences without letter 'A' or 'a'
    - Type 'quit' to exit early
    - Limited to MAX_ATTEMPTS tries
    
    Example Interaction:
        Attempt 1/10 (or 'quit'): hello world
        ✅ New record: 11 characters!
        Attempt 2/10 (or 'quit'): bad sentence
        ❌ Contains 'A'. Try again.
        Attempt 3/10 (or 'quit'): quit
        
        🏆 Best sentence (11 chars):
           'hello world'
    """
    print("\n🥇 Exercise 5: No 'A' Challenge")
    print(f"🎯 Challenge: Type sentences WITHOUT the letter 'A'")
    print(f"⚠️ Maximum {MAX_ATTEMPTS} attempts\n")
    
    best_sentence = ""
    attempts = 0
    
    while attempts < MAX_ATTEMPTS:
        attempts += 1
        sentence = input(f"Attempt {attempts}/{MAX_ATTEMPTS} (or 'quit'): ").strip()
        
        if sentence.lower() == "quit":
            break
            
        if 'a' in sentence.lower():
            print("❌ Contains 'A'. Try again.")
            continue
            
        if len(sentence) > len(best_sentence):
            best_sentence = sentence
            print(f"✅ New record: {len(best_sentence)} characters!")
        else:
            print(f"⏸️ No new record. Current: {len(best_sentence)}")
    
    if best_sentence:
        print(f"\n🏆 Best sentence ({len(best_sentence)} chars):")
        print(f"   '{best_sentence}'")
    else:
        print("\n😔 No valid sentences recorded.")


def main() -> None:
    """Run all Ninja exercises in sequence."""
    exercise_1_2_terminal_concepts()
    exercise_3_boolean_outputs()
    exercise_4_text_length()
    exercise_5_no_a_challenge()


if __name__ == "__main__":
    main()