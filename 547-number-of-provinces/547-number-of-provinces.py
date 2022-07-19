class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = self.bfs(isConnected)
        return ans
    def bfs(self, M):
        visited = {i:False for i in range(len(M))}
        print(visited)
        ans = 0
        for i in range(len(M)):
            if visited[i] == False:
                ans += 1
                visited[i] = True
                q = collections.deque()
                q.append(i)
                while q:
                    now = q.popleft()
                    for j in range(len(M)):
                        if M[now][j] == 1 and visited[j] == False:
                            q.append(j)
                            visited[j] = True
        return ans
    