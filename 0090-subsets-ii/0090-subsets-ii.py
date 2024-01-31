class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        self.helper(0, nums, [], ans, False)
        return ans
    
    def helper(self, start, nums, cur, ans, prev):
        if start == len(nums):
            ans.append(cur)
            return
        
        if start > 0 and nums[start] == nums[start-1] and not prev:
            self.helper(start+1, nums, cur, ans, False)
        else:
            self.helper(start+1, nums, cur+[nums[start]], ans, True)
            self.helper(start+1, nums, cur, ans, False)
            
            
        
        
        
        
   
        