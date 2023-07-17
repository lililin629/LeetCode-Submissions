class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            f = 0
            s = 1
            while s < len(nums):
                if nums[f] == nums[s]:
                    f += 2
                    s += 2
                else:
                    return nums[f]
            return nums[f]
                
        