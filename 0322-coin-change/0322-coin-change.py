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
        
#         def dfs(rem):
#             if rem < 0:
#                 return -1
#             if rem == 0:
#                 return 0
#             if rem not in d:
#                 min_cost = float('inf')
#                 for coin in coins:
#                     res = dfs(rem - coin)
#                     if res != -1:
#                         min_cost = min(min_cost, res + 1)
#                 d[rem] = min_cost if min_cost != float('inf') else -1
#             return d[rem]
        
#         d = defaultdict(int)
#         d[0] = 0
#         return dfs(amount)
        
                
        