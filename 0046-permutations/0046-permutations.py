class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        ans = []
        for a in self.permute(nums[1:]):
            for i in range(len(a)+1):
                ans.append(a[:i]+[nums[0]]+a[i:])
        return ans
           
            
            
        