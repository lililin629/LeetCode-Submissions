# class Solution:
#     def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
#         ans = []
#         for i in range(len(graph)):
#             for node in graph[i]:
#                 if not self.safe(graph, node):
#                     break
#             ans.append(i)
#         return ans
        
#     def safe(self, graph, node):
#         if len(graph[node]) == 0:
#             return True
#         for child in graph[node]:
#             if not self.safe(graph, child):
#                 return False
#         return True
        
class Solution:
    def eventualSafeNodes(self, graph) -> List[int]:
        def isSafe(node):
            if state[node] != 0:
                return state[node] == 2
            state[node] = 1
            for neighbor in graph[node]:
                if not isSafe(neighbor):
                    return False
            state[node] = 2
            return True

        state = [0] * len(graph)  # 0: unvisited, 1: visiting, 2: safe
        ans = []
        for i in range(len(graph)):
            if isSafe(i):
                ans.append(i)
        return ans
            
                    
        