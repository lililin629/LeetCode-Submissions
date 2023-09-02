class DSU:
    # self.par[i] < 0 if i is an ultimate parent 
    def __init__(self):
        self.par = [-1]*100001   
    def find(self, x):
        if self.par[x] >= 0:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
        return x
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        elif self.par[px] < self.par[py]:
            if self.par[py] < -1:
                self.par[px] += self.par[py]
            else:
                self.par[px] -= 1
            self.par[py] = px
        else:
            if self.par[px] < -1:
                self.par[py] += self.par[px]
            else:
                self.par[py] -= 1
            self.par[px] = py
            
        return True
    
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU()
       
        for [x, y] in edges:
            dsu.union(x, y)
#             print(dsu.par[x])
#             print(dsu.par[y])
            
        
        components = []
        for i in range(n):
            # print(dsu.par[i])
            if dsu.par[i] < 0:
                components.append(-dsu.par[i])
        ans = 0
        remaining = n
        for comp in components:
            remaining -= comp
            ans += comp*remaining
            
        return ans
                
            
        
                
        