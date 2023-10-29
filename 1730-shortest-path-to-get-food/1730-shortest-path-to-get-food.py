class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        pq = deque()
       
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    pq.append((i, j))
                    break
                  
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        cur_dist = 0
        
        while pq:
            l = len(pq)
            cur_dist += 1
            for _ in range(l):
                curx, cury = pq.popleft()
                for dx, dy in dirs:
                    nx, ny = curx+dx, cury+dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 'O':
                            pq.append((nx, ny))
                            grid[nx][ny] = '2'
                        elif grid[nx][ny] == '#':
                            return cur_dist
        return -1
                            
                        
                    
            
        
        