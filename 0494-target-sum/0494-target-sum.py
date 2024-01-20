class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        self.memo = {}
        self.nums = nums
        return self.dp(n, target)
    
    def dp(self, n, target):   
        if n == 0:
            if target == 0:
                return 1
            else:
                return 0
        if (n, target) not in self.memo:
            t1 = target - self.nums[n-1]
            t2 = target + self.nums[n-1]
            self.memo[(n, target)] = self.dp(n-1, t1) + self.dp(n-1, t2)
        return self.memo[(n, target)]
        
        