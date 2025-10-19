"""Module: test_tictactoe
Purpose: Regression tests for the Day 5 tic-tac-toe mini project.
Author: Kevin Cusnir "Lirioth"
Created: 2025-10-19
Last Updated: 2025-10-19
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
GAME_PATH = PROJECT_ROOT / "Exercises" / "TicTacToe" / "tictactoe.py"


def load_module(module_name: str, relative_path: Path) -> object:
    """Register and execute the target module so helpers can be tested."""
    spec = importlib.util.spec_from_file_location(module_name, str(relative_path))
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module {module_name} from {relative_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


tictactoe = load_module("day5_tictactoe", GAME_PATH)


class TicTacToeHelpersTests(unittest.TestCase):
    """Unit coverage for pure helper functions in tictactoe.py."""

    def test_new_board_starts_empty(self) -> None:
        """A freshly created board should contain only single spaces."""
        board = tictactoe.new_board()
        self.assertEqual(len(board), 3)
        self.assertTrue(all(cell == " " for row in board for cell in row))

    def test_parse_move_happy_path(self) -> None:
        """Input like '2 3' should map to zero-based coordinates."""
        self.assertEqual(tictactoe.parse_move("2 3"), (1, 2))

    def test_parse_move_invalid_format(self) -> None:
        """Non-two-token strings should raise ValueError."""
        with self.assertRaises(ValueError):
            tictactoe.parse_move("23")

    def test_validate_move_guards(self) -> None:
        """validate_move should reject occupied or out-of-range squares."""
        board = tictactoe.new_board()
        board[0][0] = "X"
        with self.assertRaises(ValueError):
            tictactoe.validate_move(board, "1 1")
        with self.assertRaises(ValueError):
            tictactoe.validate_move(board, "4 1")

    def test_check_win_conditions(self) -> None:
        """check_win returns True for row, column, and diagonal victories."""
        row_board = [
            ["X", "X", "X"],
            [" ", "O", " "],
            ["O", " ", " "],
        ]
        self.assertTrue(tictactoe.check_win(row_board, "X"))

        col_board = [
            ["O", "X", " "],
            ["O", "X", " "],
            [" ", "X", " "],
        ]
        self.assertTrue(tictactoe.check_win(col_board, "X"))

        diag_board = [
            ["X", "O", " "],
            [" ", "X", "O"],
            [" ", " ", "X"],
        ]
        self.assertTrue(tictactoe.check_win(diag_board, "X"))

    def test_is_tie_detection(self) -> None:
        """is_tie should return True when the board is full."""
        full_board = [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", "O"],
        ]
        self.assertTrue(tictactoe.is_tie(full_board))
        self.assertFalse(tictactoe.is_tie(tictactoe.new_board()))


if __name__ == "__main__":
    unittest.main()
