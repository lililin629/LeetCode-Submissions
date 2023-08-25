class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dirs = [(-1, 0), (0, -1)]
        heap = []
        m = len(grid)
        n = len(grid[0])
        end_data = (grid[m-1][n-1], (m-1, n-1))
        heapq.heappush(heap, end_data)
        d = {}
        for i in range(m):
            for j in range(n):
                d[(i, j)] = float('inf')
        d[(m-1, n-1)] = grid[m-1][n-1]
        
     
        while heap:
    
            cur = heapq.heappop(heap)
            curx, cury = cur[1]
            
            for dx, dy in dirs:
                neix, neiy = curx + dx, cury + dy
                if 0 <= neix < m and 0 <= neiy < n:
                    if d[(curx, cury)]+grid[neix][neiy] < d[(neix, neiy)]:
                        d[(neix, neiy)] = d[(curx, cury)]+grid[neix][neiy]
                        heapq.heappush(heap, (d[(neix, neiy)], (neix, neiy)))
        return d[(0, 0)]
                    
                    
        