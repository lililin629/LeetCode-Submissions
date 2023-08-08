class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.n = n
        self.d = defaultdict(list)
        # build graph
        for [u, v] in edges:
            self.d[u].append(v)
            self.d[v].append(u)
            
        
        # traverse
        visited = set()
        if not self.dfs(0, -1, visited):
            return False
        
        return (len(visited) == n)
        
        
    def dfs(self, start, parent, visited):
        
        if start in visited:
            return False
        visited.add(start)
        
        
        for nex in self.d[start]:
            if nex != parent and not self.dfs(nex, start, visited):
                return False
        return True
        
        