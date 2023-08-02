class Solution:
    def search(self, nums: List[int], target: int) -> int:
        end = nums[-1]
        
        l = 0
        r = len(nums)-1
        
        if target == end:
            return r
        
        while l + 1 < r:
            m = (l + r)//2
            if nums[m] == target:
                return m
            if target > end:
                if nums[m] > target:
                    r = m
                if nums[m] < end:
                    r = m
                if nums[m] < target and nums[m] > end:
                    l = m
            else:
                if nums[m] > end:
                    l = m
                if nums[m] < target:
                    l = m
                if nums[m] > target and nums[m] < end:
                    r = m
                
                
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1
    
   
        