class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums)-1
        max_sum = 0
        while i < j:
            if nums[i] + nums[j] >= k:
                j -= 1
            else:
                if nums[i] + nums[j] > max_sum:
                    max_sum = nums[i] + nums[j]
                i += 1
            
        if max_sum == 0:
            return -1
        else:
            return max_sum
            
        