class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        
        while l + 1 < r:
            mid = (l+r)//2
            if self.need(mid) == n:
                return mid
            elif self.need(mid) > n:
                r = mid
            else:
                l = mid
        if self.need(l) == n:
            return l
        elif self.need(r) == n:
            return r
        else:
            return l
        
        
        
    def need(self, n):
        return (1 + n)*n//2
            
        
        