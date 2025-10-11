"""
File: menumanager.py
Role: Data layer for the Restaurant Menu Manager. Handles loading/saving JSON,
      and pure menu operations (add/remove). 🚦📄
Note: This module owns the JSON path (encapsulation). The UI shouldn't know it. 🧠
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional


@dataclass
class MenuManager:
    """Manage a simple restaurant menu backed by a JSON file. 🍽️💾"""
    filepath: str = "restaurantmenu.json"  # UI shouldn't care about this path 🧱
    menu: Dict[str, List[Dict[str, object]]] = field(default_factory=lambda: {"items": []})

    def __post_init__(self) -> None:
        path = Path(self.filepath)
        if not path.exists():
            # Seed with an empty structure if missing (UI may still show "no items") 🌱
            path.write_text(json.dumps({"items": []}, indent=2), encoding="utf-8")
        self._load()

    # ---------- Core I/O ----------
    def _load(self) -> None:
        """Load menu from disk into memory. 📥"""
        with open(self.filepath, "r", encoding="utf-8") as f:
            self.menu = json.load(f)
        # Normalize structure just in case 🔧
        self.menu.setdefault("items", [])

    def save_to_file(self) -> None:
        """Persist current in-memory menu back to JSON file. 📤"""
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.menu, f, indent=2, ensure_ascii=False)
        print("✅ Menu saved to file.")

    # ---------- Operations ----------
    def add_item(self, name: str, price: float) -> bool:
        """Add a new item (no immediate save). Returns True if added. ➕"""
        name = name.strip()
        if not name:
            return False
        try:
            price_val = float(price)
        except (TypeError, ValueError):
            return False
        # If same name exists, replace price (idempotent UX) ♻️
        idx = self._find_index(name)
        if idx is not None:
            self.menu["items"][idx]["price"] = price_val
        else:
            self.menu["items"].append({"name": name, "price": price_val})
        return True

    def remove_item(self, name: str) -> bool:
        """Remove an item by name (case-insensitive). Returns True if removed. ➖"""
        idx = self._find_index(name)
        if idx is None:
            return False
        # Use del operator as hinted 🗑️
        del self.menu["items"][idx]
        return True

    def list_items(self) -> List[Dict[str, object]]:
        """Return a shallow copy of items for read-only UI. 📃"""
        return list(self.menu.get("items", []))

    # ---------- Internals ----------
    def _find_index(self, name: str) -> Optional[int]:
        target = name.strip().lower()
        for i, it in enumerate(self.menu.get("items", [])):
            if str(it.get("name", "")).strip().lower() == target:
                return i
        return None
