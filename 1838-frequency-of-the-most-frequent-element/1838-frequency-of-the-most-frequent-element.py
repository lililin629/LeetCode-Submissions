class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        maxf = 0
        nums.sort()
        total = nums[l]
        
        while r < len(nums):
            f = r-l+1
        
            if total + k >= nums[r]*f:
                maxf = max(f, maxf)
                r += 1
                if r < len(nums):
                    total += nums[r]
            else:
                total -= nums[l]
                l += 1
                
        return maxf
            
                
                
        