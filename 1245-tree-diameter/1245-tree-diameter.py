class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        # build graph
        self.g = defaultdict(list)
        for [u, v] in edges:
            self.g[u].append(v)
            self.g[v].append(u)
            
       
        # bfs from any node find the first peripheral node1
        self.dist = 0
        self. visited = set()
        node1 = self.bfs(0)
        
        self.dist = -1
        self. visited = set()
        node2 = self.bfs(node1)
    
        return self.dist
    
    def bfs(self, node):
        last_node = None
        q = deque([node])
        while q:
            self.dist += 1
            l = len(q)
            for i in range(l):
                cur = q.popleft()
                last_node = cur
                self.visited.add(cur)
                for c in self.g[cur]:
                    if c not in self.visited:
                        q.append(c)
        return last_node
            
        
        
        # bfs from node1 to find the second node
        
        
        
        # for each child, calculate the longest distance to leaf and treeDiameter
        # record top 2 dist1, dist2, top treeDiameter
        # return max(dist1 + dist2, dia1)
        
        
        
        