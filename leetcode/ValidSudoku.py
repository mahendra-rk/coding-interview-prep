# Leetcode
# 36. Valid Sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isRowValid(board) and self.isColumnValid(board) and self.isSquareValid(board)
    
    def isRowValid(self, board):
        for row in board:
            if not self.isUnitValid(row):
                return False # return False if any of the rows is invalid.
        return True # default to returning True if none of the rows are invalid.
            
    def isColumnValid(self, board):
        for row in zip(*board): # zip(*iterator) to create transpose of matrix
            if not self.isUnitValid(row):
                return False
        return True
            
    def isSquareValid(self, board):
        for i in (0, 3, 6): # x coordinates start values
            for j in (0, 3, 6): # y coordinates start values 
                square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)] # nums in sqaure
                if not self.isUnitValid(square):
                    return False
        return True
        
    def isUnitValid(self, unit):
        nums = [num for num in unit if num != "."] # filter out "."
        return len(set(nums)) == len(nums)
        