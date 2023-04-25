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
    
    def getOptionsFor(self, r: int, c: int) -> list[int]:
        return self.puzzle[r][c].getOptions()
    
    def reset(self, r: int, c: int) -> None:
        old_value = self.puzzle[r][c].get()
        self.puzzle[r][c].reset()
        self.__syncReset(r, c, old_value)
    
    def isValid(self) -> bool:
        # A simplified version of the isSolved logic
        # Check that there are no duplicates in 1) a row 2) a col 3) a subsection
    
        # row check
        for r in range(9):
            seen = set()
            for c in range(9):
                value = self.puzzle[r][c].get()
                if (value is None):
                    continue
                
                if (value in seen):
                    return False
                
                seen.add(value)
            
        # col check
        for c in range(9):
            seen = set()
            for r in range(9):
                value = self.puzzle[r][c].get()
                if (value is None):
                    continue
                
                if (value in seen):
                    return False
                
                seen.add(value)
            
        
        subsquares = [[set(), set(), set()] for _ in range(3)]
        for r in range(9):
            for c in range(9):
                row_index = r // 3
                col_index = c // 3
                
                value = self.puzzle[r][c].get()
                if (value is None):
                    continue

                if (value in subsquares[row_index][col_index]):
                    return False
                
                subsquares[row_index][col_index].add(value)
        
        return True
                

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
        
    def solve(self) -> bool:
        print('called')
        if (not self.isValid()):
            print('bad')
            return False
        
        if self.isSolved():
            return True

        for r in range(9):
            for c in range(9):
                
                # Skip over the spots that already have values
                if self.puzzle[r][c].isSet():
                    continue

                options = self.getOptionsFor(r, c)
                for option in options:
                    # set
                    self.set(r, c, option)

                    # recurse
                    if self.solve():
                        return True
                    
                    # unset
                    self.reset(r, c)

        return False
                