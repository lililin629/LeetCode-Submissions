class Solution:
    def climbStairs(self, n: int) -> int:
        return self.dp(n)
        
    
    @cache
    def dp(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.dp(n-2) + self.dp(n-1)
        
        