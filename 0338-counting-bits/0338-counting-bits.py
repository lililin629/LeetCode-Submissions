class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            n = self.count(i)
            ans.append(n)
        return ans
    
    def count(self, i):
        n = 0
        while i > 0:
            n += i%2
            i >>= 1
        
        return n
        