# 🥷 Exercises XP Ninja - Expert Function Challenges

Four advanced exercises demonstrating professional-grade function design, string processing, and algorithm implementation.

## 📊 Quick Stats

- **Difficulty**: 🥇 Advanced  
- **Time Required**: 120-180 minutes  
- **Exercises**: 4 expert-level challenges  
- **Concepts**: Smart capitalization, Morse code translation, box printing, sorting algorithms  
- **Prerequisites**: ExercisesXP and ExercisesXPGold completed

## 🎓 Learning Objectives

- ✅ Implement smart string capitalization with special characters
- ✅ Build bidirectional translation systems (English ⇄ Morse)
- ✅ Create dynamic text formatting with variadic functions (`*args`)
- ✅ Understand and implement the Insertion Sort algorithm
- ✅ Apply strict validation and error handling
- ✅ Design pure, testable functions

## 🚀 Quick Start

```bash
cd Exercises/ExercisesXPNinja
python xpninjafunctionssingle.py
```

## 📋 Exercise Breakdown

### 1️⃣ Full Name Builder 🧑‍🤝‍🧑

**Goal**: Build full names with optional middle names and smart capitalization.

**Features**:
- Handles hyphens and apostrophes (e.g., `o'connor-smith` → `O'Connor-Smith`)
- Optional middle name parameter
- Proper capitalization of all components

**Example**:
```python
get_full_name("john", "hooker", "lee")  # "John Hooker Lee"
get_full_name("bruce", last_name="lee") # "Bruce Lee"
```

---

### 2️⃣ Morse Code Translator 📻

**Goal**: Translate between English and Morse code with strict validation.

**Features**:
- Letters separated by spaces
- Words separated by ` / `
- Supports letters, numbers, and punctuation
- Raises `ValueError` for unsupported characters

**Examples**:
```python
text_to_morse("SOS HELP 123")
# '... --- ... / .... . .-.. .--. / .---- ..--- ...--'

morse_to_text("... --- ... / .... . .-.. .--.")
# 'SOS HELP'
```

**Supported Characters**: A-Z, 0-9, common punctuation

---

### 3️⃣ Box Printer ⭐

**Goal**: Print text in a star-framed box with dynamic sizing.

**Features**:
- Accepts any number of strings with `*args`
- Auto-adjusts width to longest string
- Returns framed string for reusability

**Example Output**:
```
******************
* Hello          *
* World          *
* in             *
* reallylongword *
* a              *
* frame          *
******************
```

---

### 4️⃣ Insertion Sort 🧠

**Goal**: Implement the Insertion Sort algorithm in-place.

**Algorithm**:
- **Best Case**: O(n) when nearly sorted
- **Average/Worst**: O(n²)
- **Stable**: Maintains relative order of equal elements
- **In-place**: Sorts without extra arrays

**Example**:
```python
arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(arr)
print(arr)  # [17, 20, 26, 31, 44, 54, 55, 77, 93]
```

**How It Works**: Like sorting playing cards in your hand - pick each card and insert it into its correct position.

---

## 💡 Key Concepts Demonstrated

### Variadic Functions
```python
def box_printer(*strings):
    # Accepts any number of arguments
    pass
```

### String Processing
- Smart capitalization with `split()` and `join()`
- Character mapping with dictionaries
- Format string alignment

### Error Handling
```python
if char not in morse_dict:
    raise ValueError(f"Unsupported character: {char}")
```

### Algorithm Analysis
- Time complexity: O(n²) for Insertion Sort
- Space complexity: O(1) - in-place sorting
- Stability considerations

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| Capitalization issues | Check hyphen/apostrophe handling in `_cap_hyphen_apostrophe()` |
| Morse translation fails | Verify character is in supported set |
| Box width incorrect | Check padding calculation with longest string |
| Sort not working | Ensure list is mutable (not tuple) |

### Best Practices

- **🧪 Test edge cases**: Empty strings, special characters, single elements
- **✅ Validate input**: Raise errors early for invalid data
- **📝 Document assumptions**: What characters are supported?
- **🔧 Design for reuse**: Return values, don't just print

---

## 🎯 Success Criteria

- [ ] **Exercise 1**: Handle all capitalization cases correctly
- [ ] **Exercise 2**: Translate bidirectionally without errors
- [ ] **Exercise 3**: Box adapts to any number/length of strings
- [ ] **Exercise 4**: Sort works on various array sizes and states
- [ ] **Overall**: Code is clean, tested, and well-documented

---

## 🚀 Next Steps

1. ✅ Optimize Insertion Sort or try other algorithms (Merge Sort, Quick Sort)
2. ✅ Extend Morse code to support more characters
3. ✅ Add color to box printer output
4. ✅ Implement unit tests for all functions
5. ✅ Apply these patterns to the Daily Challenge

---

## 📚 Additional Resources

- [Sorting Algorithms Visualized](https://visualgo.net/en/sorting)
- [Morse Code Standards](https://en.wikipedia.org/wiki/Morse_code)
- [Python *args and **kwargs](https://realpython.com/python-kwargs-and-args/)

---

**Author**: Kevin Cusnir 'Lirioth'  
**Repository**: [Fullstack2026](https://github.com/Lirioth/Fullstack2026)  
**Week 1 Day 4** - Functions - Exercises XP Ninja
