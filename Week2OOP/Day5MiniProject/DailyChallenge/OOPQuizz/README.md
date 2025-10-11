
# 🧠 Daily Challenge: OOP Quizz + 🃏 Deck of Cards (Python)

Welcome! This mini‑repo covers **Exercise 1 (OOP theory)** and **Exercise 2 (Deck implementation)**.  
It’s small, clean, and beginner‑friendly — perfect for pushing to GitHub and submitting to DI Learning. ✨

---

## 📚 Exercise 1 — OOP Questions (Short & Clear)

- **What is a class?** 🏗️ A blueprint that defines data (attributes) and behavior (methods) shared by its objects.
- **What is an instance?** 🧩 A concrete object created from a class with its own identity and state.
- **What is encapsulation?** 🔒 Bundling data and methods together while controlling access (in Python by convention: public / _protected / __name‑mangled). Keeps invariants safe.
- **What is abstraction?** 🎭 Exposing only the essential interface and hiding unnecessary details — focus on *what* it does, not *how*.
- **What is inheritance?** 🧬 Creating a new class from an existing one to reuse/extend behavior (**is‑a** relationship).
- **What is multiple inheritance?** 🧵 A class inherits from more than one base class. Useful but needs a clear lookup order.
- **What is polymorphism?** 🦎 “Many forms”: the same operation works on different types via a shared interface (overriding, duck typing).
- **What is MRO (Method Resolution Order)?** 🧭 The order Python uses to look up attributes/methods. Python uses **C3 linearization**. Check with `Class.__mro__` or `Class.mro()`.

---

## 🃏 Exercise 2 — Deck of Cards (No Inheritance from Card)

- `Card` ✅ immutable dataclass with:
  - **suit**: `"Hearts" | "Diamonds" | "Clubs" | "Spades"`  
  - **value**: `"A,2,3,4,5,6,7,8,9,10,J,Q,K"`  
  - Validated upon creation.
- `Deck` ✅ plain class with:
  - `shuffle()` → rebuilds all **52** cards and shuffles randomly.
  - `deal()` → removes and returns **one** card.
  - `deal_many(n)` → returns **n** cards safely.
  - `len(deck)` → remaining cards.
  - `iter(deck)` → iterate remaining cards.

> Requirement check: The **Deck** class does **not** inherit from `Card`. ✔️

---

## 🚀 Quickstart

**Prereqs:** Python 3.10+

```bash
# 1) Run the demo
python demo.py

# 2) Or run the module directly
python deck.py

# 3) Run unit tests (standard library only)
python -m unittest
```

**Example output:**  
```
🃏 Shuffled a fresh deck of 52 cards!
🖐️ Dealt a 5-card hand:
 - 7 of Hearts
 - K of Clubs
 - A of Spades
 - 10 of Diamonds
 - 3 of Clubs
📦 Cards left in deck: 47
```

---

## 🧩 Files & Structure

```text
oop_quizz_deck_kevin/
├─ deck.py        # Card + Deck classes with shuffle(), deal(), deal_many()
├─ demo.py        # Tiny script to showcase usage
├─ tests/
│  └─ test_deck.py  # unittest-based tests (no external deps)
└─ README.md
```

---

## 🧪 Mini API Reference

- `Card(suit, value)` → immutable; raises `ValueError` on invalid input.  
  👉 `str(Card("Spades", "A"))` ➜ `"A of Spades"`
- `Deck()` → starts as a full (sorted) deck of 52.
- `Deck.shuffle()` → resets to 52 and shuffles 🔀
- `Deck.deal()` → returns a `Card`, removes it from the deck.
- `Deck.deal_many(n)` → returns `list[Card]` of length `n`.
- `len(deck)` → remaining count.
- `for card in deck:` → iterate remaining cards.

---

## 🧷 Submission Tips (DI)

1. **Push to GitHub** 📤 — commit with a clear message:
   ```bash
   git add .
   git commit -m "Daily Challenge: OOP Quizz + Deck of Cards"
   git push origin main
   ```
2. **Submit to DI Learning** ✅ — paste your repo link.
3. (Optional) Add a screenshot of your test results for bonus clarity. 📸

---

## 📝 Notes

- No third‑party libraries are used — everything is standard library.
- Logging is enabled (INFO). You can change to DEBUG for more details.
- The code is intentionally simple and readable for learning purposes.
