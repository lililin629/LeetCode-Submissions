class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            dir = [(1, 0),(0, 1),(-1, 0),(0, -1)]
            q = deque([(i, j)])
            while q:
                cur_x, cur_y = q.popleft()
                for dx, dy in dir:
                    x, y = cur_x + dx, cur_y + dy
                    if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]):
                        if grid[x][y] == '1':
                            grid[x][y] = '0'
                            q.append((x, y))
                                

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    bfs(i, j)
        return count
        
        
        