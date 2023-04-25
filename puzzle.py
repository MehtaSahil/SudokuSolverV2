from square import Square
from typing import Optional


class Puzzle:
    def __init__(self, grid: list[list[int]]):
        self.puzzle = [ [None]*9 for _ in range(9)]
        for r in range(9):
            for c in range(9):
                s = Square(r, c, grid[r][c])
                self.puzzle[r][c] = s

    def set(self, r: int, c: int, value: int) -> None:
        self.puzzle[r][c].set(value)
    
    def get(self, r: int, c: int) -> Optional[int]:
        return self.puzzle[r][c].get()
    
    def reset(self, r: int, c: int) -> None:
        self.puzzle[r][c].reset()
    
    def isSolved(self) -> bool:
        return False