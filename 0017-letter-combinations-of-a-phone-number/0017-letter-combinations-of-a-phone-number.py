class Solution:
    def __init__(self):
        self.d = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],
             '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],
             '8':['t','u','v'], '9':['w','x','y','z'] }
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        if len(digits) == 1:
            return self.d[digits[0]]
        ans = []
        for s in self.letterCombinations(digits[1:]):
            for ch in self.d[digits[0]]:
                ans.append(ch+s)
        return ans


     
        

        