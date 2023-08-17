class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        dic = {')':'(', 
               ']':'[',
               '}':'{'}
        for ch in s:
            if ch in dic:
                if st and st[-1] == dic[ch]:
                    st.pop()
                else:
                    return False
            else:
                st.append(ch)
        if not st:
            return True
        return False
                
                
        
        
        
        
        
        
        
#         self.st = []
#         # FILO
#         for ch in s:
#             if ch == '(' or ch == '{' or ch == '[':
#                 self.st.append(ch)
#             if ch == ')':
#                 if self.check(ch, '('):
#                     continue
#                 return False
#             if ch == ']':
#                 if self.check(ch, '['):
#                     continue
#                 return False
#             if ch == '}':
#                 if self.check(ch, '{'):
#                     continue
#                 return False
                
            
#         if len(self.st) != 0:
#             return False
#         return True
    
#     def check(self, ch, lp):
#         if self.st and self.st[-1] == lp:
#             self.st.pop()
#             return True
#         return False
        
            
                
            
        