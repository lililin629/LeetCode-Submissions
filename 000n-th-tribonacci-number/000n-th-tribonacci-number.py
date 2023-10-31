class Solution:
    def tribonacci(self, n: int) -> int:
        self.memo = dict()
        return self.helper(n)
    
    def helper(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        if n not in self.memo:
            self.memo[n] = self.helper(n-1)+self.helper(n-2)+self.helper(n-3)
        
        return self.memo[n]
        