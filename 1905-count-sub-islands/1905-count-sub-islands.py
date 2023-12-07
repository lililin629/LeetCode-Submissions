class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    grid2[i][j] = 2
                    if self.bfs(grid1, grid2, i, j, m, n):
                        ans += 1
        return ans
                        
    def bfs(self, grid1, grid2, i, j, m, n):
        is_sub = True
        q = deque([(i, j)])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while q:
            cx, cy = q.popleft()
            if grid1[cx][cy] != 1:
                is_sub = False
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n and grid2[nx][ny] == 1:
                    q.append((nx, ny))
                    grid2[nx][ny] = 2
        return is_sub
                
                
        
        
        
        