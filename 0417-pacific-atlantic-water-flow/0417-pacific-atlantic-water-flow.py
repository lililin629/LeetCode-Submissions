class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific = [[None] * n for _ in range(m)]
        atlantic = [[None] * n for _ in range(m)]

        qp = deque()
        qa = deque()
        for i in range(m):
            pacific[i][0] = True
            qp.append((i, 0))
            atlantic[i][n-1] = True
            qa.append((i, n-1))

        for i in range(n):
            pacific[0][i] = True
            qp.append((0, i))
            atlantic[m-1][i] = True
            qa.append((m-1, i))
        
        self.bfs(qp, m, n, heights, pacific)
        self.bfs(qa, m, n, heights, atlantic)

        ans = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])
        return ans

    
    def bfs(self, q, m, n, heights, map):
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            cx, cy = q.popleft()
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if nx < m and nx >= 0 and ny < n and ny >= 0:
                    if heights[nx][ny] >= heights[cx][cy]:
                        if not map[nx][ny]:
                            q.append((nx, ny))
                            map[nx][ny] = True
        