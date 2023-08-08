class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        d = defaultdict(list)
        
        #build graph
        for edge in edges:
            d[edge[0]].append(edge[1])
            d[edge[1]].append(edge[0])
        
        # global
        self.diameter = 0
        
        # it's an undirected connected component, starting from anywhere is the same
        root = 0
        visited = set()
        
        # get the diameter of each node
        self.dfs(root, d, visited)
        return self.diameter
    
    
    def dfs(self, root, d, visited):
        long1, long2 = 0, 0
        visited.add(root)
        if not d[root]:
            return 0
        
        for node in d[root]:
            if node not in visited:
                cur_dia = self.dfs(node, d, visited)+1
                if cur_dia > long1:
                    long2 = long1
                    long1 = cur_dia
                    continue
                if cur_dia > long2:
                    long2 = cur_dia
        self.diameter = max(self.diameter, long1+long2)
        return long1
        
        
            
            
            
            
        
        
        
        
        
            
            
        
        