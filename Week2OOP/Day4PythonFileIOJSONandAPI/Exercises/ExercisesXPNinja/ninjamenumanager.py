"""
File: ninjamenumanager.py
Role: Data layer for Restaurant Menu Manager (Valentine rules with RegEx). 💘📄
Encapsulation: This file owns the JSON path & structure; UI shouldn't care. 🧱
"""

from __future__ import annotations

import json, re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional


VAL_CONNECTION_WORDS = {"of", "the", "and", "a", "an", "for", "with", "to", "in", "on", "at", "by", "from", "or"}  # 🔡
PRICE_PATTERN = re.compile(r"^\d{2},14$")  # e.g., 23,14 ✅


def _heart_lines(width: int = 30) -> List[str]:
    """Return an ASCII heart made of '*' for display. ❤️
    The math: two semicircles + triangle-ish bottom.
    """
    heart = []
    n = width // 2
    # top lobes
    for y in range(n//2, n, 2):
        line = ""
        for x in range(0, n*2+1):
            # Eq of two circles: (x-n)^2 + (y-n)^2 <= r^2 approximated
            cx1 = (x - (n//2))**2 + (y - (n//2))**2
            cx2 = (x - (3*n//2))**2 + (y - (n//2))**2
            r2 = (n//2)**2
            line += "*" if (cx1 <= r2 or cx2 <= r2) else " "
        heart.append(line.rstrip())
    # bottom
    for y in range(n, 0, -1):
        pad = " " * (n - y)
        stars = "*" * (2*y + (n//2))
        heart.append((pad + stars).rstrip())
    return heart


def validate_valentine_name(name: str) -> bool:
    """Validate Valentine item name via rules. 🧪
    Rules:
      • Each *space-separated* word starts uppercase, except connection words (lowercase). 🧠
      • First word must start with capital 'V'. 🔤
      • Contains at least two 'e' letters (any case). 🅴
      • No digits allowed. 🚫🔢
      • Hyphenated tokens allowed (e.g., 'Valentines-day'); we only enforce the first sub-token capitalized.
    """
    if any(ch.isdigit() for ch in name):
        return False
    if sum(1 for ch in name.lower() if ch == "e") < 2:
        return False

    tokens = name.strip().split()
    if not tokens:
        return False

    # First token must start with 'V'
    if not tokens[0] or tokens[0][0] != "V":
        return False

    for tok in tokens:
        if tok.lower() in VAL_CONNECTION_WORDS:
            if tok != tok.lower():
                return False  # connection words must be lowercase
            continue
        # Allow hyphen: check first sub-token capitalized
        subtoks = tok.split("-")
        first = subtoks[0]
        if not first or not first[0].isupper():
            return False
        # remaining subtokens can be any case (example shows 'Valentines-day')
        if not all(sub.replace("-", "").isalpha() for sub in subtoks):
            pass
    return True


@dataclass
class NinjaMenuManager:
    """Manage menu + Valentine specials with validation & regex. 🍽️🌹"""
    filepath: str = "restaurantmenu.json"
    menu: Dict[str, List[Dict[str, object]]] = field(default_factory=lambda: {"items": [], "valentines": []})

    def __post_init__(self) -> None:
        path = Path(self.filepath)
        if not path.exists():
            path.write_text(json.dumps({"items": [], "valentines": []}, indent=2, ensure_ascii=False), encoding="utf-8")
        self._load()

    # ---------- I/O ----------
    def _load(self) -> None:
        with open(self.filepath, "r", encoding="utf-8") as f:
            self.menu = json.load(f)
        self.menu.setdefault("items", [])
        self.menu.setdefault("valentines", [])

    def save_to_file(self) -> None:
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.menu, f, indent=2, ensure_ascii=False)
        print("✅ Menu saved to JSON.")

    # ---------- Regular items ----------
    def add_item(self, name: str, price: float) -> bool:
        name = name.strip()
        try:
            price_val = float(price)
        except Exception:
            return False
        # Update or append
        for it in self.menu["items"]:
            if str(it.get("name")).strip().lower() == name.lower():
                it["price"] = price_val
                return True
        self.menu["items"].append({"name": name, "price": price_val})
        return True

    def remove_item(self, name: str) -> bool:
        target = name.strip().lower()
        for i, it in enumerate(self.menu["items"]):
            if str(it.get("name")).strip().lower() == target:
                del self.menu["items"][i]  # del per spec 🗑️
                return True
        return False

    # ---------- Valentine specials ----------
    def add_valentine_item(self, name: str, price_text: str) -> bool:
        """Validate and add to valentines; persist immediately. 💘📌"""
        if not validate_valentine_name(name):
            return False
        if not PRICE_PATTERN.fullmatch(price_text):
            return False
        self.menu["valentines"].append({"name": name.strip(), "price": price_text})
        self.save_to_file()
        return True

    # ---------- Pretty heart ----------
    @staticmethod
    def heart_ascii() -> str:
        return "\n".join(_heart_lines())

    # ---------- Read-only ----------
    def list_all(self) -> Dict[str, List[Dict[str, object]]]:
        return {"items": list(self.menu.get("items", [])), "valentines": list(self.menu.get("valentines", []))}
