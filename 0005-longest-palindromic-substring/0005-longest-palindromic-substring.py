class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = defaultdict(int)
        mx = 1
        ret = s[0]
        for i in range(len(s)):
            dp[(i,i)] = 1
        for j in range(len(s)-1):
            if s[j] == s[j+1]:
                dp[(j,j+1)] = 1
                mx = 2
                ret = s[j:j+2]
        
        for length in range(2, len(s)):
            for start in range(0, len(s)-length):
                end = start + length
                if s[start] == s[end] and dp[(start+1, end-1)]:
                    dp[(start, end)] = 1
                    if end-start+1 > mx:
                        mx = end-start+1
                        ret = s[start:end+1]
        return ret
                    
                
                
            
            
        