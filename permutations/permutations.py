class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        self.dfs(nums, [], set(), ans)
        return ans
    
    def dfs(self, nums, cur, used, ans):
        if len(cur) == len(nums):
            ans.append(list(cur))
            return
        for i in range(len(nums)):
            if nums[i] in used:
                continue
            cur.append(nums[i])
            used.add(nums[i])
            self.dfs(nums, cur, used, ans)
            used.remove(nums[i])
            cur.pop()
        