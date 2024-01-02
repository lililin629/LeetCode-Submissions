class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]
                
        ans = []
        
        if nums[0] > lower:
            ans.append([lower, nums[0]-1])
        
        l = 0
        r = 1
        while l < r < len(nums):
            if nums[r] - nums[l] > 1:
                ans.append([nums[l]+1, nums[r]-1])
            l += 1
            r += 1
        
        if nums[-1] < upper:
            ans.append([nums[-1]+1, upper])
        return ans
                    
                
            
                
            
        