#!/usr/bin/env python3
"""Module: caesarcipher
Purpose: Day 3 gold challenge implementing Caesar cipher helpers and a CLI.
Author: Kevin Cusnir 'Lirioth'
Created: 2025-10-18
Last Updated: 2025-10-19

Features:
    - Encrypt and decrypt with any integer shift while preserving case
    - Leave non-letter characters unchanged
    - Interactive text UI for learners
    - Optional CLI arguments for scripted usage
"""

from __future__ import annotations
import argparse
from typing import Iterable

ALPHABET_SIZE = 26

def _shift_char(ch: str, shift: int) -> str:
    """Shift an ASCII letter while preserving case.

    Args:
        ch: Character to transform.
        shift: Number of positions to move (can be negative).

    Returns:
        Shifted character with wrapping. Non-letters are returned unchanged.
    """
    if 'A' <= ch <= 'Z':
        base = ord('A')
        return chr((ord(ch) - base + shift) % ALPHABET_SIZE + base)
    if 'a' <= ch <= 'z':
        base = ord('a')
        return chr((ord(ch) - base + shift) % ALPHABET_SIZE + base)
    return ch

def encrypt(text: str, shift: int) -> str:
    """Encrypt plaintext by shifting letters forward.

    Args:
        text: Source message to encrypt.
        shift: Number of positions to move each letter.

    Returns:
        Ciphertext with letters shifted, leaving other characters intact.
    """
    return ''.join(_shift_char(c, shift) for c in text)

def decrypt(text: str, shift: int) -> str:
    """Decrypt ciphertext by reversing the shift.

    Args:
        text: Ciphertext to decode.
        shift: Original shift value used during encryption.

    Returns:
        Plaintext recovered by applying the opposite shift.
    """
    return encrypt(text, -shift)

def brute_force(text: str) -> Iterable[str]:
    """Yield all 26 possible decryptions labeled with their shift.

    Args:
        text: Ciphertext to inspect.

    Yields:
        Candidate plaintext strings prefixed with their shift number.
    """
    for s in range(ALPHABET_SIZE):
        yield f"shift={s:2d}: {decrypt(text, s)}"

def _ask_int(prompt: str) -> int:
    """Prompt until an integer is entered.

    Args:
        prompt: Prompt message for the learner.

    Returns:
        Valid integer supplied by the user.
    """
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            # ⚠️ Reinforce that only integer values are accepted for shifts.
            print("Please enter an integer (e.g., 3 or -5).")


def interactive_main() -> None:
    print("""
== Caesar Cipher ==
Choose an option:
  [E] Encrypt
  [D] Decrypt
  [B] Brute-force (try all 26 shifts)
  [Q] Quit
""".strip())
    while True:
        choice = input("Mode (E/D/B/Q): ").strip().lower()
        if choice in ("q", "quit", "exit"):
            print("Goodbye!")
            return
        elif choice in ("e", "encrypt"):
            text = input("Enter plaintext: ")
            shift = _ask_int("Enter shift (integer): ")
            print("\nCiphertext:\n" + encrypt(text, shift) + "\n")
        elif choice in ("d", "decrypt"):
            text = input("Enter ciphertext: ")
            shift = _ask_int("Enter shift used (integer): ")
            print("\nPlaintext:\n" + decrypt(text, shift) + "\n")
        elif choice in ("b", "brute", "bruteforce"):
            text = input("Enter ciphertext to brute-force: ")
            print("\nPossible plaintexts:")
            for line in brute_force(text):
                print(line)
            print()
        else:
            print("Unknown option. Please choose E, D, B or Q.")


def cli_main() -> None:
    parser = argparse.ArgumentParser(description="Caesar cipher encrypt/decrypt/brute-force.")
    parser.add_argument("--mode", choices=["encrypt", "decrypt", "brute"], help="Operation mode.")
    parser.add_argument("--shift", type=int, default=3, help="Shift amount (ignored in brute mode). Default=3.")
    parser.add_argument("--text", type=str, help="Input text.")
    args = parser.parse_args()

    if not args.mode:
        # No CLI options provided; fall back to interactive mode.
        interactive_main()
        return

    if args.mode in ("encrypt", "decrypt") and args.text is None:
        parser.error("--text is required for encrypt/decrypt modes.")
    if args.mode == "brute" and args.text is None:
        parser.error("--text is required for brute mode.")

    if args.mode == "encrypt":
        print(encrypt(args.text, args.shift))
    elif args.mode == "decrypt":
        print(decrypt(args.text, args.shift))
    elif args.mode == "brute":
        for line in brute_force(args.text):
            print(line)


if __name__ == "__main__":
    # If launched with any CLI flags, use argparse; otherwise, show the interactive menu.
    import sys
    if len(sys.argv) > 1:
        cli_main()
    else:
        interactive_main()
