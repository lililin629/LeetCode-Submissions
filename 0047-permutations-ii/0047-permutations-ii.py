class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        cur = tuple()
        used = set()
        seen = set()
        ans = []
        self.helper(0, nums, cur, used, seen, ans)
        return ans
    
    def helper(self, ind, nums, cur, used, seen, ans):
        if len(cur) == len(nums):
            if cur not in seen:
                seen.add(cur)
                ans.append(list(cur))
        
        for i in range(len(nums)):
            if i not in used:
                used.add(i)
                self.helper(ind+1, nums, cur+(nums[i],), used, seen, ans)
                used.remove(i)
                
      
        
        