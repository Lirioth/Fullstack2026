"""
File: ninjamenueditor.py
Role: UI for Ninja Restaurant Manager (Valentine rules + heart). 🧑‍🍳💘
Note: Calls only NinjaMenuManager methods (encapsulation). 🧱
"""

from __future__ import annotations

from ninjamenumanager import NinjaMenuManager, validate_valentine_name, PRICE_PATTERN


def show_menu(manager: NinjaMenuManager) -> None:
    """Print regular + Valentine menus with a heart. ❤️"""
    print("\n" + manager.heart_ascii())
    data = manager.list_all()
    print("\n--- Regular Menu ---")
    for it in data["items"]:
        print(f"- {it['name']} — ₪{it['price']}")
    print("\n--- Valentine Specials ---")
    for it in data["valentines"]:
        print(f"- {it['name']} — {it['price']}")  # price text like XX,14
    print()


def add_valentine_flow(manager: NinjaMenuManager) -> None:
    """Ask manager for Valentine item (name + price), validate via regex, and save. 🌹"""
    name = input("Valentine item name: ").strip()
    price = input("Valentine price (format XX,14): ").strip()
    if manager.add_valentine_item(name, price):
        print("Added to Valentine specials. ✅")
    else:
        # Provide hints
        ok_name = validate_valentine_name(name)
        ok_price = bool(PRICE_PATTERN.fullmatch(price))
        print("⚠️ Could not add item.")
        if not ok_name:
            print("  • Name rules: start with 'V', connection words lowercase, ≥2 'e', no digits.")
        if not ok_price:
            print("  • Price must match pattern: XX,14")


def add_regular_flow(manager: NinjaMenuManager) -> None:
    """Add or update a regular item. ➕"""
    name = input("Item name: ").strip()
    try:
        price = float(input("Item price (number): ").strip())
    except Exception:
        print("⚠️ Price must be numeric.")
        return
    if manager.add_item(name, price):
        print("Item added/updated. ✅")
    else:
        print("⚠️ Failed to add item.")


def remove_regular_flow(manager: NinjaMenuManager) -> None:
    """Remove a regular item. ➖"""
    name = input("Item name to remove: ").strip()
    if manager.remove_item(name):
        print("Item removed. 🗑️")
    else:
        print("⚠️ Item not found.")


def main() -> None:
    m = NinjaMenuManager()
    while True:
        print("=== Ninja Menu Manager ===")
        print("1) Show menu ❤️")
        print("2) Add Valentine item 🌹")
        print("3) Add regular item ➕")
        print("4) Remove regular item ➖")
        print("5) Save & Exit 💾🚪")
        choice = input("Choose (1-5): ").strip()
        if choice == "1":
            show_menu(m)
        elif choice == "2":
            add_valentine_flow(m)
        elif choice == "3":
            add_regular_flow(m)
        elif choice == "4":
            remove_regular_flow(m)
        elif choice == "5":
            m.save_to_file()
            print("Saved. Bye! 👋")
            break
        else:
            print("⚠️ Invalid choice.\n")


if __name__ == "__main__":
    main()
