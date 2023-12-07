class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        
        
        for coin in coins:
            total = coin
            while total <= amount:
                dp[total] = min(dp[total], dp[total-coin]+1)
                total += 1
        return dp[amount] if dp[amount] != float('inf') else -1