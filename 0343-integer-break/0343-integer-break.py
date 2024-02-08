class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = [0] * (n + 1)
        dp[1] = 1  # Base case, the product of breaking number 1 is 1 (not used directly)

        for i in range(2, n + 1):
            for j in range(1, i):
                # For each j, check if we should break it further or not
                # Compare not breaking i-j further (just j*(i-j)) or breaking it further (j*dp[i-j])
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
                
        return dp[n]
        
# class Solution:
#     def integerBreak(self, n: int) -> int:
#         self.memo = defaultdict(int)
#         max_p = 0
#         for k in range(2, n+1):
#             self.mp = 0
#             self.helper(k, n, 1)
#             max_p = max(max_p, self.mp)
#         return max_p
    
#     def helper(self, k, n, cur):
#         if k > n:
#             return
#         if n < 0:
#             return 
#         if k < 0:
#             return 
#         if k == 0 and n == 0:
#             self.mp = max(cur, self.mp)
        
#         for i in range(1, n+1):
            
#             self.helper(k-1, n-i, cur*i)
            
            
        