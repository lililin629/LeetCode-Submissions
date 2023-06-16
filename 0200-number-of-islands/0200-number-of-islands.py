class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    self.bfs(i, j, grid) # change connected grids to 2
        return count
                    
        
    def bfs(self, i, j, grid):
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque([(i, j)])
        
        grid[i][j] = "2"
        
        while queue:
            cur_x, cur_y = queue.popleft()
            for dx, dy in dirs:
                nx, ny = cur_x + dx, cur_y + dy
                if nx >= 0 and ny >= 0 and nx < len(grid) and ny < len(grid[0]):
                    if grid[nx][ny] == "1":
                        grid[nx][ny] = "2"
                        queue.append((nx, ny))
                    
                
        
        
                    
                            
                        
                    
                
                
        