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
                    self.bfs(grid, visited, i, j, m, n)
        return count
    
    def bfs(self, grid, visited, i, j, m, n):
        q = deque([(i, j)])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            cx, cy = q.popleft()
            for (dx, dy) in dirs:
                nx, ny = cx + dx, cy + dy
                if (nx, ny) not in visited and 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                    q.append((nx, ny))
                    visited.add((nx, ny))
                    
                    
         
        
        
        
            
        
        
        
        
        
        
            
        
        