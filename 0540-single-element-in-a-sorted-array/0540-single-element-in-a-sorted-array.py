class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        start = 0
        end = len(nums) - 1
        return self.rec(nums, start, end)
    
    def rec(self, nums, start, end):
        if start == end:
            return nums[start]
        
        mid = (start + end)//2
        left = nums[mid-1]
        ele = nums[mid]
        right = nums[mid+1]
        if left != ele and right != ele:
            return ele
        elif left == ele:
            if mid%2 == 0:
                end = mid-1
            else:
                start = mid+1
        else:
            if mid%2 == 0:
                start = mid+1
            else:
                end = mid-1
        return self.rec(nums, start, end)


            
