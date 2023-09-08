# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         n = len(cost)
#         dp = [0]*(n+1)
       
#         for i in range(2, n+1):
#             dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
#         return dp[n]
    
        
#######################################SOL 2####################################      
        
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int: 
        n = len(cost)
        self.cost = cost
        return self.dfs(n)
    
    @cache
    def dfs(self, n):
        if n == 0 or n == 1:
            return 0
        if n == 2:
            return min(self.cost[0], self.cost[1])
        c1 = self.dfs(n-1) + self.cost[n-1]
        c2 = self.dfs(n-2) + self.cost[n-2]
        return min(c1, c2)
        
        