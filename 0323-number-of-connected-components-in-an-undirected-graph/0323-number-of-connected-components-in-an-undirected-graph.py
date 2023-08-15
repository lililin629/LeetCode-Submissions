class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for [u, v] in edges:
            g[u].append(v)
            g[v].append(u)
        
        count = 0
        visited = set()
        
        for i in range(n):
            if i not in visited:
                q = deque([i])
                count += 1

                while q:
                    cur = q.popleft()
                    visited.add(cur)
                    for node in g[cur]:
                        if node not in visited:
                            q.append(node)
        return count
            
            
            
        