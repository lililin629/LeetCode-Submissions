class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        # partition 1
        while left <= right:
            while left <= right and nums[left] < 1:
                left += 1
            while left <= right and nums[right] >= 1:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        # partition 2
        left = 0
        right = len(nums) - 1
        # partition 1
        while left <= right:
            while left <= right and nums[left] < 2:
                left += 1
            while left <= right and nums[right] >= 2:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
       