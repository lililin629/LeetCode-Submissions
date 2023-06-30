class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        return self.dfs(n, dp)

    def dfs(self, n, dp):
        if n == 0 or n == 1:
            return 1

        else:
            if n in dp:
                return dp[n]
            dp[n] = self.dfs(n-1, dp) + self.dfs(n-2, dp)
            return dp[n]
        