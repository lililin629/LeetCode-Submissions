class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        nums.sort()
        target = sum(nums) // 2
        memo = {}  # Memoization dictionary
        return self.helper(nums, 0, 0, target, memo)

    def helper(self, nums, idx, cur, target, memo):
        if cur == target:
            return True
        if cur > target or idx >= len(nums):
            return False
        if (idx, cur) in memo:  # Check if result is already computed
            return memo[(idx, cur)]

        # Choose the current number
        include = self.helper(nums, idx + 1, cur + nums[idx], target, memo)

        # Skip the current number
        exclude = self.helper(nums, idx + 1, cur, target, memo)

        # Store the result in the memo and return
        memo[(idx, cur)] = include or exclude
        return memo[(idx, cur)]

        