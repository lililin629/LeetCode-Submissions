class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = [(num, i) for i, num in enumerate(nums)]
        sorted_nums.sort()
        
        l = 0
        r = len(nums)-1
        
        while l < r:
            lnum, lidx = sorted_nums[l]
            rnum, ridx = sorted_nums[r]
            if lnum + rnum == target:
                return [lidx, ridx]
            elif lnum + rnum < target:
                l += 1
            else:
                r -= 1
        
        
        