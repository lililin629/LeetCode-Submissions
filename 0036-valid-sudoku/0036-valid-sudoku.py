class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        # can't have duplicate numbers in a row
        for row in range(rows):
            seen = set()
            for col in range(cols):
                if not self.check(row, col, seen, board):
                    return False
                
        # can't have dupicate numbers in a col
        for col in range(cols):
            seen = set()
            for row in range(rows):
                if not self.check(row, col, seen, board):
                    return False
            
        # can't have duplicate numbers in a square
        for row in range(0, rows, 3):
            for col in range(0, cols, 3):
                seen = set()
                for i in range(row, row+3):
                    for j in range(col, col+3):
                        if not self.check(i, j, seen, board):
                            return False
                    
                        
        return True
    def check(self, i, j, seen, board):
        if board[i][j] in seen:
            return False
        if board[i][j] != '.':
            seen.add(board[i][j])
        return True

                    
        