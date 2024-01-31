class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        self.helper(0, s, ans, '')
        return ans
    
    def helper(self, start, s, ans, cur):
        if len(cur) == len(s):
            ans.append(cur)
        if start >= len(s):
            return
        if len(cur) - start < 0:
            return
        
        if s[start].isalpha():    
            self.helper(start+1, s, ans, cur+s[start].lower())
            self.helper(start+1, s, ans, cur+s[start].upper())
        else:
            self.helper(start+1, s, ans, cur+s[start])
            


