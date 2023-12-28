class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l + 1 < r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid 
            else:
                l = mid 
        # print(l)
        # print(r)
        if nums[r] == target:
            return r
        if nums[l] == target:
            return l
        if nums[r] < target:
            return r + 1
        if nums[l] < target < nums[r]:
            return r
        if nums[l] > target:
            return l
                
    
    
        
        