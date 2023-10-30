class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans = []
        self.safe_d = defaultdict(int)
        self.graph = graph
        for i in range(len(graph)):
            if self.safe(i):
                ans.append(i)
        return ans
    
    def safe(self, node):
        # 1: safe
        # 2: visited
        # -1: unsafe
        if self.safe_d[node] == 1:
            return True
        if self.safe_d[node] == -1:
            return False
        if self.safe_d[node] == 2:
            return False
        
        self.safe_d[node] = 2
        for child in self.graph[node]:
            if not self.safe(child):
                self.safe_d[node] = -1
                return False
        self.safe_d[node] = 1
        return True
     

            
                    
        