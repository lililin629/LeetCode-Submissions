class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        for i in range(n-k):
            nums.append(nums[i])
        for i in range(n-k):
            ele = nums[0]
            nums.remove(ele)