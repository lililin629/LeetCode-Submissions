class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # find the rotted 
        fresh = 0
        start = []
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    fresh += 1
                if grid[x][y] == 2:
                    start.append((x, y))
        
        if not fresh:
            return 0
        if not start:
            return -1

            
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        q = deque(start)
        time = 0
        
        while q:
            if not fresh:
                return time
            time += 1
            for _ in range(len(q)):
                curx, cury = q.popleft()
                for dx, dy in dirs:
                    nx, ny = curx + dx, cury + dy
                    if self.valid(nx, ny, m, n):
                        if grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            fresh -= 1
                            q.append((nx, ny))
        
        if not fresh:
            return time
        else:
            return -1
        
    def valid(self, x, y, m, n):
        if x >= 0 and x < m and y >= 0 and y < n:
            return True
        return False
                        
            
        