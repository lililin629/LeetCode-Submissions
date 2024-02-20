class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # BFS from gates
        m = len(rooms)
        n = len(rooms[0])
        
        starts = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    starts.append((i, j))
        print(starts)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for i, j in starts:
            q = deque()
            visited = set()
            q.append((i, j))
            visited.add((i, j))
            dist = 0
            
            while q:
                l = len(q)
                dist += 1
                for _ in range(l):
                    ci, cj = q.popleft()
                    for dx, dy in dirs:
                        nx, ny = ci + dx, cj + dy
                        if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                            if rooms[nx][ny] > dist:
                                rooms[nx][ny] = dist
                                q.append((nx, ny))
                                visited.add((nx, ny))
        
                        
                        
                        
            
                    
        