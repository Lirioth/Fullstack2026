"""
File: exercisesxpninjainheritance.py
Purpose: Single-file implementation of Conway's Game of Life using inheritance. 🧠🧬
Author: Kevin "Lirioth" Cusnir
Date: 2025-10-09 | TZ: Asia/Jerusalem

Content:
  • GameOfLife (fixed borders) — base class
  • ExpandingGameOfLife (ever-expandable up to max_size) — subclass
  • A few built-in seeds (block, blinker, glider) and demo runners

Notes:
  - Display occurs after each generation.
  - The end state is fully determined by the initial state; we detect extinction, stability, and loops.
  - Expanding mode grows the grid outward when live cells reach borders, up to max_size. 🏁
"""

from __future__ import annotations

from typing import Iterable, List, Sequence, Set, Tuple


Coord = Tuple[int, int]  # (row, col)


class GameOfLife:
    """Conway's Game of Life with fixed borders.

    Rules:
      - Any live cell with fewer than two live neighbours dies (underpopulation).
      - Any live cell with two or three live neighbours lives on to the next generation.
      - Any live cell with more than three live neighbours dies (overpopulation).
      - Any dead cell with exactly three live neighbours becomes a live cell (reproduction).

    This base class enforces fixed borders: any activity beyond the edge is ignored.
    """

    ALIVE = 1
    DEAD = 0
    ALIVE_CHAR = "█"
    DEAD_CHAR = "."

    def __init__(self, rows: int, cols: int, *, seed: Iterable[Coord] = ()) -> None:
        if rows <= 0 or cols <= 0:
            raise ValueError("rows and cols must be positive.")
        self.rows = int(rows)
        self.cols = int(cols)
        self.grid: List[List[int]] = [[self.DEAD for _ in range(self.cols)] for _ in range(self.rows)]
        for r, c in seed:
            if 0 <= r < self.rows and 0 <= c < self.cols:
                self.grid[r][c] = self.ALIVE

        # For loop detection
        self._seen: Set[Tuple[Tuple[int, ...], ...]] = set()
        self.generation = 0

    # ---------- Core mechanics ----------
    def in_bounds(self, r: int, c: int) -> bool:
        return 0 <= r < self.rows and 0 <= c < self.cols

    def neighbors_alive(self, r: int, c: int) -> int:
        count = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r + dr, c + dc
                if self.in_bounds(rr, cc) and self.grid[rr][cc] == self.ALIVE:
                    count += 1
        return count

    def next_grid(self) -> List[List[int]]:
        """Compute the next generation for a fixed-size grid."""
        nxt = [[self.DEAD for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                alive = self.grid[r][c] == self.ALIVE
                n = self.neighbors_alive(r, c)
                if alive and (n == 2 or n == 3):
                    nxt[r][c] = self.ALIVE
                elif not alive and n == 3:
                    nxt[r][c] = self.ALIVE
                else:
                    nxt[r][c] = self.DEAD
        return nxt

    def step(self) -> None:
        """Advance one generation (fixed borders)."""
        self.grid = self.next_grid()
        self.generation += 1

    # ---------- Utilities ----------
    def as_hash(self) -> Tuple[Tuple[int, ...], ...]:
        return tuple(tuple(row) for row in self.grid)

    def is_all_dead(self) -> bool:
        return all(cell == self.DEAD for row in self.grid for cell in row)

    def display(self) -> None:
        print(f"Generation {self.generation}")
        for row in self.grid:
            print("".join(self.ALIVE_CHAR if x == self.ALIVE else self.DEAD_CHAR for x in row))
        print()

    def run(self, max_generations: int = 50, *, show: bool = True, detect_loops: bool = True) -> str:
        """Run until extinction, loop/stability, or max_generations reached.
        
        Returns a short status string describing the ending.
        """
        if show:
            self.display()
        while self.generation < max_generations:
            state = self.as_hash()
            if detect_loops:
                if state in self._seen:
                    return "Loop detected 🔁"
                self._seen.add(state)

            if self.is_all_dead():
                return "All cells dead ☠️"

            prev_state = state
            self.step()
            if show:
                self.display()

            if detect_loops and self.as_hash() == prev_state:
                return "Stable (no change) ✅"

        return "Generation limit reached ⏳"


class ExpandingGameOfLife(GameOfLife):
    """Game of Life that can grow outward when activity hits borders.

    Growth strategy:
      - Before computing the next generation, if any live cell is within `margin`
        cells of any border, pad the grid by `pad` cells on all sides (if under max_size).
      - This approximates an "ever-expanding" universe without infinite memory.
    """

    def __init__(self, rows: int, cols: int, *, seed: Iterable[Coord] = (), max_size: int = 10_000, pad: int = 1, margin: int = 1) -> None:
        super().__init__(rows, cols, seed=seed)
        self.max_size = int(max_size)
        self.pad = int(pad)
        self.margin = int(margin)

    def _needs_expand(self) -> bool:
        top = any(self.grid[0][c] == self.ALIVE for c in range(self.cols))
        bottom = any(self.grid[self.rows - 1][c] == self.ALIVE for c in range(self.cols))
        left = any(self.grid[r][0] == self.ALIVE for r in range(self.rows))
        right = any(self.grid[r][self.cols - 1] == self.ALIVE for r in range(self.rows))

        if self.margin > 0:
            # Check within margin as well
            for m in range(self.margin):
                if self.rows > 2 and (any(self.grid[m][c] == self.ALIVE for c in range(self.cols)) or any(self.grid[self.rows-1-m][c] == self.ALIVE for c in range(self.cols))):
                    return True
                if self.cols > 2 and (any(self.grid[r][m] == self.ALIVE for r in range(self.rows)) or any(self.grid[r][self.cols-1-m] == self.ALIVE for r in range(self.rows))):
                    return True

        return top or bottom or left or right

    def _expand(self) -> None:
        if self.rows >= self.max_size or self.cols >= self.max_size:
            return
        new_rows = min(self.rows + 2 * self.pad, self.max_size)
        new_cols = min(self.cols + 2 * self.pad, self.max_size)
        pad_top = (new_rows - self.rows) // 2
        pad_left = (new_cols - self.cols) // 2

        new_grid = [[self.DEAD for _ in range(new_cols)] for _ in range(new_rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                new_grid[r + pad_top][c + pad_left] = self.grid[r][c]

        self.grid = new_grid
        self.rows = new_rows
        self.cols = new_cols
        # Reset seen to avoid false loop detection due to size shifts
        self._seen.clear()

    def step(self) -> None:
        # Decide if we need to expand before computing next gen
        if self._needs_expand():
            self._expand()
        super().step()


# ---------- Seeds ----------
def seed_block() -> Sequence[Coord]:
    # 2x2 still life
    return [(1, 1), (1, 2), (2, 1), (2, 2)]

def seed_blinker() -> Sequence[Coord]:
    # period-2 oscillator
    return [(2, 1), (2, 2), (2, 3)]

def seed_glider() -> Sequence[Coord]:
    # classic glider
    return [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]


# ==============
# Tiny demos ✅
# ==============
if __name__ == "__main__":
    print("=== Fixed borders demo (blinker) ===")
    game1 = GameOfLife(rows=5, cols=5, seed=seed_blinker())
    status1 = game1.run(max_generations=6, show=True, detect_loops=True)
    print("Status:", status1)
    print()

    print("=== Fixed borders demo (glider hits wall, then dies) ===")
    game2 = GameOfLife(rows=10, cols=10, seed=[(r+1, c+1) for (r,c) in seed_glider()])
    status2 = game2.run(max_generations=20, show=True, detect_loops=True)
    print("Status:", status2)
    print()

    print("=== Expanding borders demo (glider) ===")
    game3 = ExpandingGameOfLife(rows=10, cols=10, seed=[(r+4, c+4) for (r,c) in seed_glider()], max_size=200)
    status3 = game3.run(max_generations=25, show=True, detect_loops=True)
    print("Status:", status3)
