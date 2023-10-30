class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        
        for num in nums:
            if num-1 not in s:
                start = num
                count = 1
                while start + 1 in s:
                    start += 1
                    count += 1
                ans = max(ans, count)
        return ans