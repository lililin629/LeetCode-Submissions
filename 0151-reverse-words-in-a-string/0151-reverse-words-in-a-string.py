class Solution:
    def reverseWords(self, s: str) -> str:
        
        lst = s.split()
        ns = ' '.join(lst[::-1])
        return ns
            
        
        