"""
File: exercisesxpninja.py
Purpose: Single-file solutions for "Exercises XP Ninja" — Classes & Objects. 🧠🐍
Author: Kevin "Lirioth" Cusnir
Date: 2025-10-09 | TZ: Asia/Jerusalem

Content:
  • Phone class with call history and simple messaging. ☎️💬

Notes:
  - Comments are in ENGLISH.
  - Minimal standard library only.
  - Run this file directly to see demos (under __main__). ✅
"""

from __future__ import annotations

from typing import Dict, List


class Phone:
    """A minimal phone model with call history and messaging.

    Args:
        phone_number: The line/number of this phone (string recommended).

    Attributes:
        call_history: List[str] of human-readable call events.
        messages: List[Dict[str, str]] of message dictionaries with keys:
                  'to', 'from', 'content'.
    """

    def __init__(self, phone_number: str) -> None:
        self.phone_number: str = str(phone_number)
        self.call_history: List[str] = []   # starts empty
        self.messages: List[Dict[str, str]] = []  # starts empty

    # ----- Calls -----
    def call(self, other_phone: "Phone") -> None:
        """Place a call to another Phone and record it in the caller's history."""
        entry = f"{self.phone_number} called {other_phone.phone_number}"
        print(entry)
        self.call_history.append(entry)

    def show_call_history(self) -> None:
        """Print the call history for this phone."""
        if not self.call_history:
            print("No calls yet.")
            return
        print(f"Call history for {self.phone_number}:")
        for i, entry in enumerate(self.call_history, start=1):
            print(f"{i}. {entry}")

    # ----- Messages -----
    def send_message(self, other_phone: "Phone", content: str) -> None:
        """Send a message to another phone and store copies on both devices.

        Each message is stored as a dict with keys: 'to', 'from', 'content'.
        """
        msg = {"to": other_phone.phone_number, "from": self.phone_number, "content": str(content)}
        # Store on sender
        self.messages.append(msg)
        # Store on receiver (copy to avoid aliasing)
        other_phone.messages.append(dict(msg))
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}: {content}")

    def show_outgoing_messages(self) -> None:
        """Print messages where this phone is the sender ('from')."""
        out = [m for m in self.messages if m["from"] == self.phone_number]
        if not out:
            print(f"No outgoing messages for {self.phone_number}.")
            return
        print(f"Outgoing messages from {self.phone_number}:")
        for i, m in enumerate(out, start=1):
            print(f"{i}. to {m['to']}: {m['content']}")

    def show_incoming_messages(self) -> None:
        """Print messages where this phone is the recipient ('to')."""
        inc = [m for m in self.messages if m["to"] == self.phone_number]
        if not inc:
            print(f"No incoming messages for {self.phone_number}.")
            return
        print(f"Incoming messages to {self.phone_number}:")
        for i, m in enumerate(inc, start=1):
            print(f"{i}. from {m['from']}: {m['content']}")

    def show_messages_from(self, other_phone: "Phone") -> None:
        """Print incoming messages that originated from a specific other phone."""
        subset = [
            m for m in self.messages
            if m["to"] == self.phone_number and m["from"] == other_phone.phone_number
        ]
        if not subset:
            print(f"No incoming messages to {self.phone_number} from {other_phone.phone_number}.")
            return
        print(f"Messages to {self.phone_number} from {other_phone.phone_number}:")
        for i, m in enumerate(subset, start=1):
            print(f"{i}. {m['content']}")

    def __repr__(self) -> str:
        return f"Phone({self.phone_number!r})"


# ===============
# Tiny demo ✅
# ===============
if __name__ == "__main__":
    a = Phone("+972-50-111-2222")
    b = Phone("+972-52-333-4444")

    # Calls
    a.call(b)
    b.call(a)
    a.show_call_history()
    b.show_call_history()

    # Messages
    a.send_message(b, "Hi! Are you coming to Be'er Sheva today?")
    b.send_message(a, "Yes, around 18:00. Need anything?")
    a.send_message(b, "Water and good vibes. 😄")

    print()
    a.show_outgoing_messages()
    a.show_incoming_messages()

    print()
    b.show_outgoing_messages()
    b.show_incoming_messages()

    print()
    a.show_messages_from(b)
    b.show_messages_from(a)
