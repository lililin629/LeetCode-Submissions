class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum()).lower()
        
        front = 0
        end = len(s)-1
        
        while front <= end:
            if s[front] == s[end]:
                front += 1
                end -= 1
            else:
                return False
        return True
        
        
        