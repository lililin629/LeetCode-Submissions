class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        zeros = []
        l = r = 0
        while r < len(nums):
            while l < len(nums) and nums[l] != 0:
                l += 1
            r = l
            while r < len(nums) and nums[r] == 0:
                r += 1
            zeros.append(r-l)
            l = r
        ans = 0
        for ct in zeros:
            count = (1+ct)*ct//2
            ans += count
        return ans
        
            
            
                
                
        