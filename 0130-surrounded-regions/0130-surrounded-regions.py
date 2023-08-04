class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

       
        m = len(board)
        n = len(board[0])
        start = []
        # find the 0's on the border
        for i in [0, m-1]:
            for j in range(n):
                if board[i][j] == "O":
                    start.append((i, j))
        
        for i in range(1, m-1):
            for j in [0, n-1]:
                if board[i][j] == 'O':
                    start.append((i, j))
                    
        # change all the islands connected to borderr to '1'
        self.bfs(start, m, n, board) 
        
        # change remaining 'O' to 'X' and change '1 back to 'O
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '1':
                    board[i][j] = 'O'


                    
    def bfs(self, start, m, n, board):
        q = deque(start)
        visited = set()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q:
            x, y = q.popleft()
            visited.add((x, y))
            board[x][y] = '1'
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx >= 0 and ny >= 0 and nx < m and ny < n and (nx, ny) not in visited:
                    if board[nx][ny] == 'O':
                        q.append((nx, ny))





