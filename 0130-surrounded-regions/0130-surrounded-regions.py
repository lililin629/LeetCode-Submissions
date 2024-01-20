class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # find the "o" on the borders
        # find all "o" connected to border "o"
        # add above to a set
        # iterate through the board, all "o" not in set should be flipped
        
        q = deque()
        visited = set()
        noFlips = set()
        
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    if board[i][j] == "O" and (i, j) not in visited:
                        q.append((i, j))
                        visited.add((i, j))
                        noFlips.add((i, j))
                        
        
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while q:
            cx, cy = q.popleft()
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    if board[nx][ny] == "O":
                        noFlips.add((nx, ny))
                        q.append((nx, ny))
                        visited.add((nx, ny))
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in noFlips:
                    board[i][j] = 'X'
                
                    
        
        
                        
                        
                
                    
                    
            
        