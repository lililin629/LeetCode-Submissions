class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m = len(grid)
        n = len(grid[0])
        visited = set()
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited.add((i, j))
                    area = self.bfs(i, j, m, n, grid, visited)
                    max_area = max(max_area, area)
        return max_area
    
    def bfs(self, x, y, m, n, grid, visited):
        area = 0
        dirs = [(1, 0),(0, 1),(-1, 0),(0, -1)]
        q = deque([(x, y)])
    
        
        while q:
            (cx, cy) = q.popleft()
            area += 1
            for dx ,dy in dirs:
                nx, ny = cx + dx, cy + dy
                if (nx, ny) not in visited and 0 <= nx < m and 0 <= ny < n: 
                    if grid[nx][ny] == 1:
                        q.append((nx, ny))
                        visited.add((nx, ny))
        return area
        