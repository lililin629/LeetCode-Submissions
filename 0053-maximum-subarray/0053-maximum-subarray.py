class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        d = defaultdict(int)
        ps = 0
        d[-1] = ps
        l = -1
        r = 0
        max_sum = float('-inf')
        
        while r < len(nums):
            ps += nums[r]
            d[r] = ps
            
            if d[r]-d[l] >= max_sum:
                max_sum = d[r]-d[l]

            if ps < 0:
                l = r
                d[l] = 0
                ps = 0
            r += 1
            
        return max_sum
            
            
        
        