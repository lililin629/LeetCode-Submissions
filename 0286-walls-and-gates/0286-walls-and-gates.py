class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        # find all gates
        gates = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    gates.append((i, j))
                    
        # bfs from gates
        q = deque(gates)
        dirs = [(1, 0),(-1, 0),(0, 1),(0, -1)]
        steps = 0
        while q:
            l = len(q)
            steps += 1
            for _ in range(l):
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if self.valid(nx, ny, m, n, rooms):  # not wall, in boundaries
                        rooms[nx][ny] = min(steps, rooms[nx][ny])
                        q.append((nx, ny))
        
    def valid(self, x, y, m, n, rooms):
        if x >= 0 and y >= 0 and x < m and y < n:
            if rooms[x][y] == 2147483647:
                return True
        return False

            
            
        