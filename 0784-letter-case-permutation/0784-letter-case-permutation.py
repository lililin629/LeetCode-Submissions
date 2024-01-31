# class Solution:
#     def letterCasePermutation(self, s: str) -> List[str]:
#         ans = set()
#         self.helper(0, s, ans, '')
#         return list(ans)
    
#     def helper(self, start, s, ans, cur):
#         if len(cur) == len(s):
#             ans.add(cur)
#         if start >= len(s):
#             return
#         if len(cur) - start < 0:
#             return
            
#         self.helper(start+1, s, ans, cur+s[start].lower())
#         self.helper(start+1, s, ans, cur+s[start].upper())


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
        if len(cur) - start < 0:
            return
        
        for i in range(start, len(s)):    
            self.helper(i+1, s, ans, cur+s[i].lower())
            self.helper(i+1, s, ans, cur+s[i].upper())
            
            

            
                
        