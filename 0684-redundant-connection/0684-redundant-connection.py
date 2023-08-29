class DSU:
    def __init__(self):
        self.par = [-1]*1001
    def find(self, x):
        if self.par[x] > 0:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
        return x
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        elif self.par[px] < self.par[py]:
            self.par[py] = px
            self.par[px] -= 1
        else:
            self.par[px] = py
            self.par[py] -= 1
        return True
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        for [v1, v2] in edges:
            if not dsu.union(v1, v2):
                return [v1, v2]
        
        

        
        
####################################### dictionary #######################################
# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:  
#         # {root:[child1, child2], child1: root, child2: root}
#         d = dict()
#         for [n1, n2] in edges:
#             if n1 in d and n2 in d: # n1, n2 have both been part of an edge before
#                 head1 = self.getContainingSet(d, n1)
#                 head2 = self.getContainingSet(d, n2)
#                 # if they have the same ultimate parent, they are in the same cycle
#                 if head1 == head2:
#                     return [n1, n2]
#                 else: # if not, perform union
#                     d[head1].update(d[head2])
#                     for node in d[head2]:
#                         d[node] = head1
                    
#             elif n1 in d:
#                 head = self.getContainingSet(d, n1)
#                 d[n2] = head
#                 d[head].add(n2)
#             elif n2 in d:
#                 head = self.getContainingSet(d, n2)
#                 d[n1] = head
#                 d[head].add(n1)
                
#             else:
#                 d[n1] = {n1, n2}
#                 d[n2] = n1
        
#     def getContainingSet(self, d, n):
#         if isinstance(d[n], set): # if n is the ultimate parent 
#             return n
#         else:
#             return d[n]
            
            
            
            
