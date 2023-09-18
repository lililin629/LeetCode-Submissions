class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m = len(grid)-1
        n = len(grid[0])-1
        heap = []
        heapq.heappush(heap, (grid[0][0], (0, 0)))
        d = {(0, 0): grid[0][0]}
        
        while heap:
            cur = heapq.heappop(heap)
            curx, cury = cur[1]
            if (curx, cury) == (m, n):
                return d[(m, n)]
            for dx, dy in dirs:
                nx, ny = curx + dx, cury + dy
                if 0 <= nx <= m and 0 <= ny <= n and (nx, ny) not in d:
                    d[(nx, ny)] = max(d[(curx, cury)], grid[nx][ny])
                    heapq.heappush(heap, (d[(nx, ny)], (nx, ny)))
        return d[(m,n)]
                    