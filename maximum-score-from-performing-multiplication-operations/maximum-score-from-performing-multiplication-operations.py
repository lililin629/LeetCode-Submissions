class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        self.memo = defaultdict(int)
        n = len(nums)
        return self.dp(0, 0, n-1, nums, multipliers)
    
    def dp(self, idx, l, r, nums, multipliers):
        m = len(multipliers)
        if idx == m:
            return 0
        if (idx, l, r) not in self.memo:
            self.memo[(idx, l, r)] = max(nums[l]*multipliers[idx]+self.dp(idx+1, l+1, r, nums, multipliers), nums[r]*multipliers[idx]+self.dp(idx+1, l, r-1, nums, multipliers))
        return self.memo[(idx, l, r)]
        
        