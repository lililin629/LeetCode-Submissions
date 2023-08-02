class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [1, max(piles)]
        l = 1
        r = max(piles)
        mini = r
        
        while l + 1 < r:
            m = (l + r)//2
            if self.valid(m, piles, h):
                mini = min(m, mini)
                r = m
            else:
                l = m
        if self.valid(l, piles, h):
                mini = min(l, mini)
        if self.valid(r, piles, h):
                mini = min(r, mini)
        return mini
        
        
        
    def valid(self, k, piles, h):    
        hours = 0
        
        for pile in piles:
            time = (pile//k if pile%k == 0 else pile//k+1)
            hours += time
        
        if hours <= h:
            return True
        else:
            return False
        
        