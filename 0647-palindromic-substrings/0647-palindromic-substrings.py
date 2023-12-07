class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = defaultdict(int) # {(start, end): 1}
        
        for i in range(len(s)):
            dp[(i, i)] = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[(i, i+1)] = 1
        
        
        
        for dif in range(2, len(s)):
            for start in range(0, len(s)-dif):
                end = start + dif
                if s[start] == s[end] and dp[(start+1, end-1)]:
                    dp[(start, end)] = 1
        
        ans = 0
        for key, val in dp.items():
            ans += val
        return ans
            
        
       
                
        