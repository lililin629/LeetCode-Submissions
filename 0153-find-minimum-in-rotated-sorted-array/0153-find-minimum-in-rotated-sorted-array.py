class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        
        while l + 1 < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m
            if nums[m] < nums[r]:
                r = m
                
        if nums[l] < nums[r]:
            return nums[l]
        return nums[r]
        
        