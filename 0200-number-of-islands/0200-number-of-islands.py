class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    count += 1
                    self.dfs(grid, visited, i, j, m, n)
        return count
    
    def dfs(self, grid, visited, i, j, m, n):
        if (i, j) in visited or i >= m or j >= n or i < 0 or j < 0 or grid[i][j] == '0':
            return
        visited.add((i, j))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for (dx, dy) in dirs:
            self.dfs(grid, visited, i+dx, j+dy, m, n)
            
        
        
        # m = len(grid)
        # n = len(grid[0])
        # visited = set()
        # count = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == '1' and (i, j) not in visited:
        #             count += 1
        #             self.bfs(grid, visited, i, j, m, n)
        # return count
    
#     def bfs(self, grid, visited, i, j, m, n):
#         q = deque([(i, j)])
#         dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         while q:
#             cx, cy = q.popleft()
#             for (dx, dy) in dirs:
#                 nx, ny = cx + dx, cy + dy
#                 if (nx, ny) not in visited and 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
#                     q.append((nx, ny))
#                     visited.add((nx, ny))
                    
                    
         
        
        
        
            
        
        
        
        
        
        
            
        
        