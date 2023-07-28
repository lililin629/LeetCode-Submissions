class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        def dfs(cur, target):
            if target == 0:
                ls = sorted(cur)
                if ls not in ans:
                    ans.append(ls)
                return
            if target < 0:
                return
            
            for c in candidates:
                cur.append(c)
                dfs(cur, target-c)
                cur.remove(c)
        
        dfs([], target)
        return ans
                
                