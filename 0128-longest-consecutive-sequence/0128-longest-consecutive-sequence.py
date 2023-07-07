class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set = set(nums)
        max_n = 0

        
        for num in nums:
            count = 1
            if num+1 in n_set:
                continue
            while num-1 in n_set:
                num -= 1
                count += 1
            max_n = max(max_n, count)
        return max_n
        