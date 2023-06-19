class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        ans = 0
        while i < len(nums)-1:
            ans += nums[i]
            i += 2
        return ans
            
        