class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        prof = 0
        while l < r < len(prices):
            if prices[l] < prices[r]:
                prof += (prices[r]-prices[l])
            l += 1
            r += 1
        return prof
            
                
            
        