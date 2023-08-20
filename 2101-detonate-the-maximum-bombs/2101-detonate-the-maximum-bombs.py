from collections import defaultdict
from typing import List

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        d = defaultdict(list)
        
        for i, [x,y,r] in enumerate(bombs):
            for j, [nx, ny, nr] in enumerate(bombs):
                if i != j:
                    if (x-nx)**2 + (y-ny)**2 <= r**2:
                        d[i].append(j)
                        
        max_total = 0
        for bomb in range(len(bombs)):
            visited = set()
            max_total = max(self.dfs(bomb, d, visited), max_total)
        return max_total
        
    def dfs(self, start, d, visited):
        visited.add(start)
       
        for b in d[start]:
            if b not in visited:
                self.dfs(b, d, visited)               
        return len(visited)

# class Solution:
#     def maximumDetonation(self, bombs: List[List[int]]) -> int:
#         d = defaultdict(list)
        
#         for i, [x,y,r] in enumerate(bombs):
#             for j, [nx, ny, nr] in enumerate(bombs):
#                 if i != j:
#                     if (x-nx)**2 + (y-ny)**2 <= r**2:
#                         d[i].append(j)
#                     if (x-nx)**2 + (y-ny)**2 <= nr**2:
#                         d[j].append(i)
#         # {0:[1, 2], 1:[0, 2], 2:[1, 3]}
#         max_total = 0
#         for bomb in d:
#             self.visited = set()
#             max_total = max(self.dfs(bomb, d, 1), max_total)
#         return max_total
        
#     def dfs(self, start, d, total):
#         if start not in d:
#             return total
#         self.visited.add(start)
#         for b in d[start]:
#             if b not in self.visited:
#                 self.dfs(b, d, total + 1)
        
        
        
                
        

            
        