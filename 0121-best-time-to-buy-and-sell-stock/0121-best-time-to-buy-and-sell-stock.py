class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      
        max_profit = 0
        min_price = float('inf')
        for pr in prices:
            if pr < min_price:
                min_price = pr
            max_profit = max(max_profit, pr - min_price)
        return max_profit
            
            
            
        