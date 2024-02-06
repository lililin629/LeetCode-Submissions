class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        self.dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and (i, j) not in visited:
                    visited.add((i, j))
                    if self.dfs(board, word, i, j, visited, m, n, 0):
                        return True
                    visited.remove((i, j))
        return False
    
    def dfs(self, board, word, i, j, visited, m, n, idx):
        
        if idx == len(word)-1:
            return True
        
        for (dx, dy) in self.dirs:
            (nx, ny) = (i+dx, j+dy)
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and board[nx][ny] == word[idx+1]:
                visited.add((nx, ny))
                if self.dfs(board, word, nx, ny, visited, m, n, idx+1):
                    return True
                visited.remove((nx, ny))
        return False
            
        
        
        
                