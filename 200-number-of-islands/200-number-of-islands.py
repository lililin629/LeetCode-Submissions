DIRECTIONS = [(0, 1), (1,0), (0, -1), (-1, 0)]
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        num_island = 0
        visited = set()
        for x in range(m):
            for y in range(n):
                if (x, y) in visited:
                    continue
                if grid[x][y] == '1':
                    num_island += 1
                    self.explore(grid, x, y, visited)
        return num_island
        
        
    def explore(self, grid, x, y, visited):
        q = collections.deque([(x,y)])
        visited.add((x, y))
        while q:
            x, y = q.popleft()
            for dx, dy in DIRECTIONS:
                new_x = x + dx
                new_y = y + dy
                if self.is_valid(grid, new_x, new_y, visited):
                    q.append((new_x, new_y))
                    visited.add((new_x, new_y))
    
    
    def is_valid(self, grid, new_x, new_y, visited):
        m = len(grid)
        n = len(grid[0])
        if not (0<= new_x < m and 0 <= new_y < n):
            return False
        if (new_x, new_y) in visited:
            return False
        if grid[new_x][new_y] == '0':
            return False
        return True
        