class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        d = defaultdict(int)
        prefix_sum = 0
        d[-1] = prefix_sum
        
        l = -1
        
        for i in range(len(nums)):
           
            prefix_sum += nums[i]
            d[i] = prefix_sum
            while prefix_sum - d[l] >= target:
                min_len = min(min_len, i-l)
                l += 1
          
        if min_len > len(nums):
            min_len = 0
        return min_len
                    
        
        
        