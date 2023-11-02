class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        
        self.dfs(ans, 0, [], target, candidates)
      
        ret = []
        for t in ans:
            ret.append(list(t))
        return ret
    
    def dfs(self, ans, idx, cur, remain, candidates):
        if remain == 0:
            
            cur.sort()
            t = tuple(cur)
            ans.add(t)
            return
        if remain < 0:
            return
        for i in range(idx, len(candidates)):
            self.dfs(ans, i, cur+[candidates[i]], remain-candidates[i], candidates)
        
        