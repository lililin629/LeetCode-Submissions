class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pac = set()
        atl = set()
        m = len(heights)
        n = len(heights[0])
        
        for i in range(m):
            pac.add((i, 0))
            atl.add((i, n-1))
        for j in range(n):
            pac.add((0, j))
            atl.add((m-1, j))
        
        pq = deque(pac)
        aq = deque(atl)
        self.bfs(heights, pq, pac)
        self.bfs(heights, aq, atl)
        ans = []
        for (x, y) in pac:
            if (x, y) in atl:
                ans.append([x, y])
        return ans
    
    def bfs(self, heights, q, reached):
        dirs = [(1, 0),(0, 1),(-1, 0),(0, -1)]
        m = len(heights)
        n = len(heights[0])
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in reached:
                    if heights[nx][ny] >= heights[x][y]:
                        reached.add((nx, ny))
                        q.append((nx, ny))
       
      
                
        
            
        