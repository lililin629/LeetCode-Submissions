# class Solution:
#     def climbStairs(self, n: int) -> int:
        
#         dp = defaultdict(int)
#         dp[1] = 1
#         dp[2] = 2
        
#         for i in range(3, n+1):
#             dp[i] = dp[i-2] + dp[i-1]
#         return dp[n]

class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = {}
        return self.dp(n)

    def dp(self, i):
        if i <= 2: 
            return i
        if i not in self.memo:
            # Instead of just returning dp(i - 1) + dp(i - 2), calculate it once and then
            # store the result inside a hashmap to refer to in the future.
            self.memo[i] = self.dp(i - 1) + self.dp(i - 2)
        
        return self.memo[i]


# class Solution:
#     def climbStairs(self, n: int) -> int:
#         memo = {}
#         return self.dp(n, memo)

#     def dp(self, i, memo):
#         if i <= 2: 
#             return i
#         if i not in memo:
#             # Instead of just returning dp(i - 1) + dp(i - 2), calculate it once and then
#             # store the result inside a hashmap to refer to in the future.
#             memo[i] = self.dp(i - 1, memo) + self.dp(i - 2, memo)
        
#         return memo[i]
        
        