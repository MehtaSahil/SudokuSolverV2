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
        self.__syncSet(r, c, value)
    
    def get(self, r: int, c: int) -> Optional[int]:
        return self.puzzle[r][c].get()
    
    def reset(self, r: int, c: int) -> None:
        old_value = self.puzzle[r][c].get()
        self.puzzle[r][c].reset()
        self.__syncReset(r, c, old_value)
    
    def isSolved(self) -> bool:
        # First make sure that all values are set
        row_values = [set()] * 9
        col_values = [set()] * 9
        for r in range(9):            
            for c in range(9):
                current_square = self.puzzle[r][c]
                if (not current_square.isSet()):
                    return False

                row_values[r].add(current_square.get())
                col_values[c].add(current_square.get())
            
            # Check that there were nine distinct elements in the row
            if (not len(row_values[r]) == 9):
                return False
        
        # Then, make sure that column are all valid
        for c in range(9):
            unique_col_elements = len(col_values[c])
            if not unique_col_elements == 9:
                return False

        return True
    
    def __syncSet(self, r: int, c: int, new_value: int) -> None:
        for c_walk in range(9):
            self.puzzle[r][c_walk].disallowOption(new_value)
        
        for r_walk in range(9):
            self.puzzle[r_walk][c].disallowOption(new_value)
        
    def __syncReset(self, r: int, c: int, removed_value: int) -> None:
        for c_walk in range(9):
            self.puzzle[r][c_walk].allowOption(removed_value)
        
        for r_walk in range(9):
            self.puzzle[r_walk][c].allowOption(removed_value)