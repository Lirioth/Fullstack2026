"""
File: menueditor.py
Role: UI layer for the Restaurant Menu Manager. Handles input/printing only. 🖥️🧑‍🍳
Note: This module does NOT know anything about the JSON path (encapsulation). 🧱
"""

from __future__ import annotations

from typing import Optional
from menumanager import MenuManager


# ---------- Factory ----------
def load_manager() -> MenuManager:
    """Create and return a MenuManager instance. 🏗️"""
    return MenuManager()


# ---------- UI Actions ----------
def show_restaurant_menu(manager: MenuManager) -> None:
    """Pretty-print the current menu. 📋"""
    items = manager.list_items()
    if not items:
        print("No items yet. Add something tasty! 😋")
        return
    print("\n--- Restaurant Menu ---")
    for it in items:
        price = it.get("price")
        price_disp = int(price) if isinstance(price, (int, float)) and float(price).is_integer() else price
        print(f"- {it.get('name')} — ₪{price_disp}")
    print("-----------------------\n")


def add_item_to_menu(manager: MenuManager) -> None:
    """Ask for name & price, then add via manager. ➕"""
    name = input("Item name: ").strip()
    price_raw = input("Item price: ").strip()
    try:
        price = float(price_raw)
    except ValueError:
        print("⚠️ Price must be a number.")
        return
    ok = manager.add_item(name, price)
    print("Item was added successfully. ✅" if ok else "⚠️ Could not add item.")


def remove_item_from_menu(manager: MenuManager) -> None:
    """Ask for name, then remove via manager. ➖"""
    name = input("Item name to remove: ").strip()
    ok = manager.remove_item(name)
    if ok:
        print("Item deleted successfully. 🗑️")
    else:
        print("⚠️ Error: item not found.")


# ---------- Main loop ----------
def show_user_menu() -> None:
    """Interactive UI loop. Exits only after saving. 🔁"""
    manager = load_manager()
    while True:
        print("=== Exercise Menu Manager ===")
        print("1) Show restaurant menu 🍽️")
        print("2) Add an item ➕")
        print("3) Remove an item ➖")
        print("4) Save & Exit 💾🚪")
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            show_restaurant_menu(manager)
        elif choice == "2":
            add_item_to_menu(manager)
        elif choice == "3":
            remove_item_from_menu(manager)
        elif choice == "4":
            manager.save_to_file()
            print("Menu saved. Goodbye! 👋")
            break
        else:
            print("⚠️ Invalid choice. Please select 1-4.\n")


if __name__ == "__main__":
    show_user_menu()
