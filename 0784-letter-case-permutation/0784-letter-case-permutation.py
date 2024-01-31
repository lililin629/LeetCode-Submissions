class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = set()
        self.helper(0, s, ans, '')
        return list(ans)
    
    def helper(self, start, s, ans, cur):
        if len(cur) == len(s):
            ans.add(cur)
        if start >= len(s):
            return
            
        
        self.helper(start+1, s, ans, cur+s[start].lower())
        self.helper(start+1, s, ans, cur+s[start].upper())
            
            
                
        