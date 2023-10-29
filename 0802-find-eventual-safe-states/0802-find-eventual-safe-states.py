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
        if self.safe_d[node] == 1:
            return True
        if self.safe_d[node] == -1:
            return False
        
        self.safe_d[node] = -1
        for child in self.graph[node]:
            if not self.safe(child):
                return False
        self.safe_d[node] = 1
        return True
     
#     def safe(self, node):
#         if not self.graph[node]:
#             self.safe_d[node] = 1
#             return True
#         for child in self.graph[node]:
#             if child == node:
#                 self.safe_d[node] = 0
#                 return False
#             if child in self.safe_d and not self.safe_d[child]:
#                 return False
#             if child not in self.safe_d:
#                 if self.safe(child):
#                     self.safe_d[child] = 1
#                 else:
#                     self.safe_d[child] = 0
#                     return False
                    
#         return True
        
# class Solution:
#     def eventualSafeNodes(self, graph) -> List[int]:
#         def isSafe(node):
#             if state[node] != 0:
#                 return state[node] == 2
#             state[node] = 1
#             for neighbor in graph[node]:
#                 if not isSafe(neighbor):
#                     return False
#             state[node] = 2
#             return True

#         state = [0] * len(graph)  # 0: unvisited, 1: visiting, 2: safe
#         ans = []
#         for i in range(len(graph)):
#             if isSafe(i):
#                 ans.append(i)
#         return ans
            
                    
        