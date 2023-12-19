class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # self.memo = defaultdict(int)
        # # {3: 1, 2: -6, 1: 227, 0: 222}
        # self.dfs(nums, 0, len(nums), 1)
        ans = self.dfs(nums, len(nums)-1)
        print(ans)
        return ans >= 0
    
    def dfs(self, nums, remain):
        if remain == 0:
            return nums[0]
        l = nums[0] - self.dfs(nums[1:], remain-1)
        r = nums[-1] - self.dfs(nums[:-1], remain-1)
        
        return max(l, r)
        
        
     
        
     
                
        