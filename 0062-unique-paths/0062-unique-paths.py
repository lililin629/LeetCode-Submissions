class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # initialize
        dp = [[1]*n for _ in range(m)]
        # recursion
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        # return
        return dp[m-1][n-1]
        