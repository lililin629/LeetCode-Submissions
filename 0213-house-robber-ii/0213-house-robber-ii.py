class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]
        self.memo = defaultdict(int)
        s1 = self.helper(nums[1:], n-2)
        self.memo = defaultdict(int)
        s2 = self.helper(nums[:n-1], n-2)
        return max(s1, s2)
        
    def helper(self, nums, n):
       
        if n == 0:
            return nums[0]
        if n == 1:
            return max(nums[0], nums[1])
       
        if n not in self.memo:
            self.memo[n] = max(self.helper(nums, n-1), self.helper(nums, n-2)+nums[n])
        return self.memo[n]    
        
        
        
        