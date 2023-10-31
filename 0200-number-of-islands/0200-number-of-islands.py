# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         count = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     count += 1
#                     self.bfs(grid, i, j)
#         return count
    
#     def bfs(self, grid, i, j):
#         q = deque()
#         q.append((i, j))
#         grid[i][j] = '2'
        
#         dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
#         while q:
#             cx, cy = q.popleft()
#             for dx, dy in dirs:
#                 nx, ny = cx + dx, cy + dy
#                 if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
#                     q.append((nx, ny))
#                     grid[nx][ny] = '2'
                    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count
    
    def dfs(self, grid, i, j):
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        grid[i][j] = '2'
        
        for dx, dy in dirs:
            nx, ny = i+dx, j+dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
                self.dfs(grid, nx, ny)
            
            
        
        
            
        
        