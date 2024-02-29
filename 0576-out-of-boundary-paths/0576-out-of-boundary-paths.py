class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        base = 10**9 + 7
        self.memo = defaultdict(int)
        count = self.dfs(m, n, maxMove, startRow, startColumn)
        return count % base
    
    
    def dfs(self, m, n, mx, sRow, sCol):
        if (mx, sRow, sCol) in self.memo:
            return self.memo[(mx, sRow, sCol)]
        if mx < 0:
            return 0
        if sRow >= m or sRow < 0 or sCol >= n or sCol < 0:
            return 1
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        count = 0
        for dx, dy in dirs:
            count += self.dfs(m, n, mx-1, sRow+dx, sCol+dy)
        self.memo[(mx, sRow, sCol)] = count
        return count
            
            
        