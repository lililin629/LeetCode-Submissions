class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.helper(0, candidates, target, [], ans)
        return ans
    
    def helper(self, ind, can, target, cur, ans):
        if sum(cur) == target:
            ans.append(list(cur))
            return
        if sum(cur) > target:
            return
        
        for i in range(ind, len(can)):
            if i != ind and can[i] == can[i-1]:
                continue
            cur.append(can[i])
            self.helper(i+1, can, target, cur, ans)
            cur.pop()
        
       
        
        