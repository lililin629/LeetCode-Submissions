# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         memo = dict()
        
#         self.helper(amount, coins, 0, 0, memo)
    
#     def helper(self, amount, coins, idx, cur_sum, memo):
#         if cur_sum == amount:
#             return 1
#         if idx >= len(coins):
#             return 0
#         if cur_sum > amount:
#             return 0
#         if (idx, cur_sum) in memo:
#             return memo[(idx, cur_sum)]
        
#         choose = self.helper(amount, coins, idx + 1, cur_sum + coins[idx], memo)
#         not_choose = self.helper(amount, coins, idx + 1, cur_sum, memo)
        
#         memo[(idx, cur_sum)] = choose + not_choose
#         return memo[(idx, cur_sum)]

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = dict()
        return self.helper(amount, coins, 0, 0, memo)
    
    def helper(self, amount, coins, idx, cur_sum, memo):
        if cur_sum == amount:
            return 1
        if idx >= len(coins) or cur_sum > amount:
            return 0
        if (idx, cur_sum) in memo:
            return memo[(idx, cur_sum)]
        
        # Choose the current coin
        choose = self.helper(amount, coins, idx, cur_sum + coins[idx], memo)
        # Do not choose the current coin
        not_choose = self.helper(amount, coins, idx + 1, cur_sum, memo)
        
        memo[(idx, cur_sum)] = choose + not_choose
        return memo[(idx, cur_sum)]

            
        