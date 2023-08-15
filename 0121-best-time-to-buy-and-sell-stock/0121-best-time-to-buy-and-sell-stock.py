class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        max_price = 0
        while r < len(prices):
            r += 1
            if r < len(prices):
                if prices[r] < prices[l]:
                    l = r
                max_price = max(max_price, prices[r] - prices[l])
        return max_price
            
            





# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
      
#         max_profit = 0
#         min_price = float('inf')
#         for pr in prices:
#             if pr < min_price:
#                 min_price = pr
#             max_profit = max(max_profit, pr - min_price)
#         return max_profit
            
            
            
        