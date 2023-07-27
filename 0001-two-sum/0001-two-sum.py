class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = []
        for i in range(len(nums)):
            new_nums.append((nums[i],i))
        new_nums.sort()
        
        l = 0
        r = len(new_nums)-1
        while l < r:
            if new_nums[l][0] + new_nums[r][0] < target:
                l += 1
            if new_nums[l][0] + new_nums[r][0] > target:
                r -= 1
            if new_nums[l][0] + new_nums[r][0] == target:
                return [new_nums[l][1], new_nums[r][1]]
                                                            
        