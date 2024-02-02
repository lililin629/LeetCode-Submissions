class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = set()
        self.dfs(nums, used, [], ans)
        return ans
    
    def dfs(self, nums, used, cur, ans):
        if len(cur) == len(nums):
            ans.append(list(cur))
            return
        
        for i in range(len(nums)):
            if nums[i] not in used:
                cur.append(nums[i])
                used.add(nums[i])
                self.dfs(nums, used, cur, ans)
                used.remove(nums[i])
                cur.pop()
        
      
        
       
        