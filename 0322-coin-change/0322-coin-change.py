class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dfs(rem):
            if rem in d:
                return d[rem]
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            min_cost = float('inf')
            for coin in coins:
                res = dfs(rem - coin)
                if res != -1:
                    min_cost = min(min_cost, res + 1)
            d[rem] = min_cost if min_cost != float('inf') else -1
            return d[rem]
        
        d = defaultdict(int)
        d[0] = 0
        return dfs(amount)
        
                
        