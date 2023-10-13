class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = defaultdict(int)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]
#         return self.dp(n)
        
    
#     @cache
#     def dp(self, n):
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         else:
#             return self.dp(n-2) + self.dp(n-1)
        
        