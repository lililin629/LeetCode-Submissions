class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.row = len(board)
        self.col = len(board[0])
        self.board = board
        for i in range(self.row):
            for j in range(self.col):
                if self.backtrack(i, j, word):
                    return True
    
    def backtrack(self, row, col, word):
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        if not len(word):
            return True
        if not self.valid(row, col, word):
            return False
        
        self.board[row][col] = '-1'
        for dx, dy in dirs:
            nr, nc = row+dx, col+ dy
            if self.backtrack(nr, nc, word[1:]):
                return True
        self.board[row][col] = word[0]
        return False
    
    def valid(self, r, c, word):
        if r >= self.row or r < 0 or c >= self.col or c < 0 or self.board[r][c] != word[0]:
            return False
        return True
                    
            
            
        
        