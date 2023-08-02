class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l + 1 < r:
            m = (l + r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m
            else:
                r = m
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1
        
        
            
        