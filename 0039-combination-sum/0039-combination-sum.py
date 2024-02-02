class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.helper(0, candidates, target, [], ans)
        return ans
        
    def helper(self, ind, candidates, target, cur, ans):
        if sum(cur) == target:
            ans.append(list(cur))
            return
        
        if sum(cur) > target:
            return
       
        for i in range(ind, len(candidates)):
            self.helper(i, candidates, target, cur+[candidates[i]], ans)
            
           
       
        