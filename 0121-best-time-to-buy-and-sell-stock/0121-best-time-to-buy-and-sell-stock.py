class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        h = 1
        maxp = 0
        
        while h < len(prices):
            if prices[h] - prices[l] > maxp:
                maxp = prices[h] - prices[l]
                
            if prices[h] < prices[l]:
                l = h
            
            h += 1
        
        return maxp
                
            
        