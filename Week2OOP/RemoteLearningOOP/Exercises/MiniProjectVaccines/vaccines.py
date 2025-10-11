
"""
💉 Vaccines Management System — Minimal OOP Solution
---------------------------------------------------
- Human: id_number, name, age, priority, blood_type, family 👨‍👩‍👧‍👦
- Queue: manage vaccination order with priority & age rules 🧭
- Neutral tone; concise comments with emojis ✨
- Bonus: avoids list.insert, list.pop, list.index, list.sort, sorted ✅
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Iterable, Tuple

BLOOD_TYPES: Tuple[str, ...] = ("A", "B", "AB", "O")


@dataclass(slots=True)
class Human:
    """Represents a citizen. 🧍

    Part 1: attributes only.
    Part 2: adds 'family' and 'add_family_member'.
    """
    id_number: str
    name: str
    age: int
    priority: bool
    blood_type: str
    # Part 2 — family members living in the same household
    family: List["Human"] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.blood_type not in BLOOD_TYPES:
            raise ValueError(f"Invalid blood type: {self.blood_type!r}. Allowed: {BLOOD_TYPES}")
        if self.age < 0:
            raise ValueError("Age must be non‑negative")

    # Part 2 — bi‑directional family link
    def add_family_member(self, person: "Human") -> None:
        """Add a family member to both sides. 🔗"""
        if person is self:
            return
        # Avoid duplicates without using list.index
        if all(member is not person for member in self.family):
            self.family.append(person)
        if all(member is not self for member in person.family):
            person.family.append(self)


class Queue:
    """Queue of humans waiting for vaccination. 🧭

    Rules:
      - add_person: seniors (age ≥ 60) or priority go to the front (index 0).
      - get_next: returns and removes the person at index 0.
      - get_next_blood_type: returns/removes first with requested blood type.
      - sort_by_age: priority first, then older (non‑priority age ≥ 60), then younger.
      - swap: exchanges the positions of two persons.
      - rearrange_queue (Part 2): avoid two family members standing consecutively when possible.

    Bonus: does NOT use list.insert, list.pop, list.index, list.sort, or sorted.
    """
    def __init__(self) -> None:
        self.humans: List[Human] = []  # starts empty ✅

    # ——— Utilities ———
    @staticmethod
    def _same_person(a: Human, b: Human) -> bool:
        # Identity OR matching id_number is considered the same person
        return (a is b) or (a.id_number == b.id_number)

    @staticmethod
    def _same_family(a: Human, b: Human) -> bool:
        # Same family if they reference each other (bi‑directional link) 🙌
        # or if one is present in the other's family list.
        if a is b:
            return True
        # Avoid list.index; use any()
        if any(member is b for member in a.family):
            return True
        if any(member is a for member in b.family):
            return True
        return False

    # ——— Core API ———
    def add_person(self, person: Human) -> None:
        """Add a human to the queue. Seniors (≥60) or priority go to front. 🧓⭐"""
        if person.age >= 60 or person.priority:
            # Put at front without list.insert: rebuild list
            self.humans = [person] + self.humans
        else:
            self.humans.append(person)

    def find_in_queue(self, person: Human) -> Optional[int]:
        """Return index of a human, or None if absent. 🔎 (no list.index)"""
        for i, h in enumerate(self.humans):
            if self._same_person(h, person):
                return i
        return None

    def swap(self, person1: Human, person2: Human) -> None:
        """Swap two persons in the queue. 🔁"""
        i = self.find_in_queue(person1)
        j = self.find_in_queue(person2)
        if i is None or j is None:
            raise ValueError("Both persons must be in the queue to swap")
        # Standard tuple swap is fine
        self.humans[i], self.humans[j] = self.humans[j], self.humans[i]

    def get_next(self) -> Optional[Human]:
        """Return and remove the next human (index 0). If empty, None. ⏭️"""
        if not self.humans:
            return None
        nxt = self.humans[0]
        # Remove first element without pop: slice away index 0
        self.humans = self.humans[1:]
        return nxt

    def get_next_blood_type(self, blood_type: str) -> Optional[Human]:
        """Return and remove the first human with the given blood type, else None. 🩸"""
        if blood_type not in BLOOD_TYPES:
            raise ValueError(f"Invalid blood type: {blood_type!r}. Allowed: {BLOOD_TYPES}")
        # Manual search (no list.index)
        i = 0
        found_idx = -1
        n = len(self.humans)
        while i < n:
            if self.humans[i].blood_type == blood_type:
                found_idx = i
                break
            i += 1
        if found_idx == -1:
            return None
        person = self.humans[found_idx]
        # Remove by rebuilding list slices
        self.humans = self.humans[:found_idx] + self.humans[found_idx+1:]
        return person

    def sort_by_age(self) -> None:
        """Reorder queue: priority first, then older (≥60), then younger. 🧮

        Stable partitioning is used (preserves relative order within groups).
        No built‑in sort/sorted.
        """
        prio: List[Human] = []
        older: List[Human] = []
        younger: List[Human] = []
        # Partition without sorting
        for h in self.humans:
            if h.priority:
                prio.append(h)
            elif h.age >= 60:
                older.append(h)
            else:
                younger.append(h)
        self.humans = prio + older + younger

    # ——— Part 2 ———
    def rearrange_queue(self) -> None:
        """Rearrange so no two consecutive persons are from the same family, if possible. 🔄

        Greedy strategy:
          1) Walk through the current queue.
          2) If the next candidate conflicts with the last in output, try to pull
             a non‑conflicting candidate from further ahead.
          3) If none exist, keep the conflicting one (unavoidable in some cases).
        """
        original = list(self.humans)  # shallow copy
        result: List[Human] = []
        while original:
            candidate = original[0]
            if not result or not self._same_family(result[-1], candidate):
                # Append candidate (no insert/pop): rebuild by slices
                result.append(candidate)
                original = original[1:]
                continue
            # Conflict: find the first non‑conflicting person ahead
            j = 1
            idx = -1
            while j < len(original):
                if not self._same_family(result[-1], original[j]):
                    idx = j
                    break
                j += 1
            if idx != -1:
                # Move that non‑conflicting person next
                pick = original[idx]
                result.append(pick)
                # Remove original[idx] by slices
                original = original[:idx] + original[idx+1:]
            else:
                # Unavoidable conflict; place candidate anyway to progress
                result.append(candidate)
                original = original[1:]
        self.humans = result


# ——— Tiny demo (optional) ———
if __name__ == "__main__":
    q = Queue()
    # Create some people 👪
    a = Human("1", "Ada", 72, False, "O")
    b = Human("2", "Ben", 34, True, "A")
    c = Human("3", "Cora", 40, False, "B")
    d = Human("4", "Dan", 67, False, "AB")
    e = Human("5", "Eve", 25, False, "O")
    # Family links
    c.add_family_member(e)  # Cora and Eve together

    # Add to queue (priority/seniors go to front)
    for p in (a, b, c, d, e):
        q.add_person(p)

    print("🧾 Initial order:", [p.name for p in q.humans])
    q.sort_by_age()
    print("🔃 After sort_by_age:", [p.name for p in q.humans])
    q.rearrange_queue()
    print("🔀 After rearrange_queue:", [p.name for p in q.humans])
    nxt = q.get_next()
    print("⏭️ get_next():", nxt.name if nxt else None)
    o_type = q.get_next_blood_type("O")
    print("🩸 get_next_blood_type('O'):", o_type.name if o_type else None)
    print("📦 Remaining:", [p.name for p in q.humans])
