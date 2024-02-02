class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1
        q = deque([(0, 0, 1)])
        visited = set([(0, 0)])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1),(-1, 1), (-1, -1)]
        
        while q:
            (cx, cy, cdis) = q.popleft()
            if (cx, cy) == (m-1, n-1):
                return cdis
            for dx, dy in dirs:
                (nx, ny, ndis) = (cx + dx, cy + dy, cdis + 1)
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                    
                    visited.add((nx, ny))
                    q.append((nx, ny, ndis))
                    
            
            
        return -1
            
        
        
        