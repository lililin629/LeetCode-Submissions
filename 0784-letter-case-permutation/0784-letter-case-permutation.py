class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = set()
        self.helper(0, s, ans, '')
        return list(ans)
    
    def helper(self, start, s, ans, cur):
        if len(cur) == len(s):
            ans.add(cur)
            
        for i in range(start, len(s)):
            self.helper(i+1, s, ans, cur+s[i].lower())
            self.helper(i+1, s, ans, cur+s[i].upper())
            
            
                
        