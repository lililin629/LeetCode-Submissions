class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        for i in range(n+1):
            self.helper(0, nums, [], i, ans)
        return ans
            
    
    def helper(self, start, nums, com, length, ans):
        if len(com) == length:
            ans.append(list(com))
        for i in range(start, len(nums)):
            com.append(nums[i])
            self.helper(i+1, nums, com, length, ans)
            com.pop()
        
        
            
            
        