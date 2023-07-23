class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # iterate through the board to find the starting char
        # dfs(start char)
        # stops when len(word) is rached or when duplicate char is used
        # check boundaries
       
        
#         def bfs(row, col, s, visited):
#             q = deque((row, col))
#             visited.add((row, col))
#             dirs = [(0,1), (0,-1), (1,0), (-1,0)]
            
#             lev = 0
#             while q:
#                 lev += 1
#                 for i in range(len(q)):
#                     curx, cury = q.popleft()
#                     s += board[curx][cury]
#                     if s != word[:lev]:
                        
#                         continue
#                     for dx, dy in dirs:
#                         nx, ny = curx+dx, cury+dy
#                         if vlid(nx, ny):
#                             q.add((nx, ny))
#                             visited.add((nx, ny))
  
        def found(used, word, x, y):
            if len(used) == len(word):
                return True
            dirs = [(0,1), (0,-1), (1,0), (-1,0)]
            f = False
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if valid(nx, ny) and word[len(used)] == board[nx][ny] and (nx, ny) not in used:
                    used.add((nx,ny))
                    f = f or found(used, word, nx, ny)
                    used.remove((nx,ny))
            return f        
                
        def valid(x, y):
            if x < len(board) and x >= 0 and y < len(board[0]) and y >= 0:
                return True
            return False
        
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0] and found({(row,col)}, word, row, col):
                    return True
        return False
#                 if board[row][col] == word[0]:
#                     visited = {(row, col)}
#                     bfs(row, col,'', visited)
       
        