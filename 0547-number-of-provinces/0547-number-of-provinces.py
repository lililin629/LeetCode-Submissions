class DSU:
    def __init__(self):
        self.par = [-1]*201
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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        dsu = DSU()
        n = len(isConnected)
        for i in range(n):
            for j in range(1, n-i):
                if isConnected[i][i+j]:
                    dsu.union(i, i+j)
        ans = 0
        for i in range(n):
            if dsu.par[i] < 0:
                ans += 1
        return ans
                    
                    