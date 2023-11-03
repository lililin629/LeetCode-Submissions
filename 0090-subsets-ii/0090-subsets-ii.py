class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        self.dfs(ans, nums, [], 0)
        ret = []
        for t in ans:
            ret.append(list(t))
        return ret
            
        
    def dfs(self, ans, nums, cur, idx):
        if idx == len(nums):
            cur.sort()
            t = tuple(cur)
            ans.add(t)
            return
        
        self.dfs(ans, nums, cur+[nums[idx]], idx+1)
        self.dfs(ans, nums, cur, idx+1)
            
        