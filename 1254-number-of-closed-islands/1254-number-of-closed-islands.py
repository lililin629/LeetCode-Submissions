class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ele = grid[i][j]
                if ele == 0:
                    c = self.bfs(i, j, grid)
                    count += c          
        return count
    
    def bfs(self, i, j, grid):
        count = 1
        queue = deque([(i, j)])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while queue:
            x, y = queue.popleft()
            if x == 0 or x == len(grid)-1 or y == 0 or y == len(grid[0])-1:
                count = 0
                
            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy
                if not (new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0])):
                    if grid[new_x][new_y] == 0:
                        queue.append((new_x, new_y))
                        grid[new_x][new_y] = 2
        return count
                    
            
                    
                    
        