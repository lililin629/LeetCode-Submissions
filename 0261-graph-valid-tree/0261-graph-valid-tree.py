class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        g = defaultdict(list)
        for [p,c] in edges:
            g[p].append(c)
            g[c].append(p)
            
        q = deque([0])
        visited = set([0])
        
        while q:
            cur = q.popleft()
            for m in g[cur]:
                if m in visited:
                    continue
                visited.add(m)
                q.append(m)
        
        return len(visited) == n
                
        
        