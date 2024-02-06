class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        d = Counter(nums)
        if 0 not in d:
            return
        
        # [1,3,12,0,0]
        l = 0
        r = 1
        while r < len(nums):
            if nums[l] == 0:
                if nums[r] != 0:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r += 1
                else:
                    r += 1
            else:
                l += 1
                r += 1
                    
        