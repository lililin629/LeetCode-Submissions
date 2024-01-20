class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0] < nums[-1]:
            return nums[0]
        l = 0
        r = n-1
        while l + 1 < r:
            mid = (l+r)//2
            val = nums[mid]
            if val < nums[l]:
                r = mid
            elif val > nums[l]:
                l = mid
        if nums[l] < nums[r]:
            return nums[l]
        else:
            return nums[r]
        
            
  
        