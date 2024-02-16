class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        ps = 0
        dp = [0]*len(arr)
        
        
        for i in range(0, len(arr)):
            for j in range(max(0, i-k+1), i+1):
                dp[i] = max(dp[j-1] + max(arr[j:i+1])*(i-j+1), dp[i])
        return dp[len(arr)-1]
            
            
        
        
        