class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # {prefix_sum: index of its first occurance}
        
        d = defaultdict(int)
        ps = 0
        d[ps] = -1
        max_len = 0
        
        for i in range(len(nums)):
            ps += nums[i]
            if ps - k in d:
                max_len = max(max_len, i-d[ps-k])
            if ps not in d:
                d[ps] = i
        return max_len
                
        
        