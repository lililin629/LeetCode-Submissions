class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # nums = [10,9,2,5,3,7,101,18]
        # (0,3), (0,3), (1,5)
        # {0:(1, 10), 1:(1, 9), 2:(1,2), 3:(2, 5) ...}
        
        d = [1]*len(nums)
        
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    d[i] = max(d[j]+1, d[i])
                
        return max(d)
            
             
                    
            
        
        