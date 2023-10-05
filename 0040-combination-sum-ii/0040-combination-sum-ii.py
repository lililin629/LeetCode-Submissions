class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combos = []
        self.helper(candidates, target, 0, [], combos)
        
        return combos
    
    def helper(self, candidates, target, idx, combo, combos):
        if target == 0:
            combos.append(list(combo))
            return 
        if target < 0:
            return
        
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                break
                
            combo.append(candidates[i])
            self.helper(candidates, target-candidates[i], i+1, combo, combos)
            combo.pop()
        
        