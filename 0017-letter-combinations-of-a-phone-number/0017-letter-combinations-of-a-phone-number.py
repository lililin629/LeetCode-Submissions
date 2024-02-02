class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
             '2':['a', 'b', 'c'],
             '3':['d', 'e', 'f'],
             '4':['g', 'h', 'i'],
             '5':['j', 'k', 'l'],
             '6':['m', 'n', 'o'],
             '7':['p', 'q', 'r', 's'],
             '8':['t', 'u', 'v'],
             '9':['w', 'x', 'y', 'z']
            }
        if not digits:
            return []
        
        ans = []
        self.helper(digits, d, 0, '', ans)
        return ans
        
    def helper(self, digits, d, ind, cur, ans):
        if len(cur) == len(digits):
            ans.append(cur)
            return
        
        for c in d[digits[ind]]:
            self.helper(digits, d, ind+1, cur+c, ans)
            
            
        