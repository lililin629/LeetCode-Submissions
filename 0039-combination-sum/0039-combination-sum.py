class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets = []
        self.dfs(candidates, 0, target, 0, [],subsets)
        return subsets
    
    def dfs(self, candidates, total, target, index, subset, subsets):
            if total == target:
                subsets.append(list(subset))
                return
            elif total > target:
                return
            for i in range(index, len(candidates)):
                subset.append(candidates[i])
               
                self.dfs(candidates, total + candidates[i], target, i, subset, subsets)
                subset.pop()
                

            

        