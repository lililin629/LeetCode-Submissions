class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.d = {
            "2":["a","b","c"],
            "3":["d","e","f"], 
            "4":["g","h","i"], 
            "5":["j","k","l"], 
            "6":["m","n","o"], 
            "7":["p","q","r","s"], 
            "8":["t","u","v"], 
            "9":["w","x","y","z"]
            }
        combos = []
        self.dfs(digits, 0, '', combos)
        return combos
    
    def dfs(self, digits, idx, combo, combos):
        
        if idx == len(digits):
            combos.append(combo)
            return
        
        for ch in self.d[digits[idx]]:
            self.dfs(digits, idx+1, combo+ch, combos)
            
        
        
        