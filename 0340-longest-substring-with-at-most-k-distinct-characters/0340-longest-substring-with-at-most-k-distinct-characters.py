class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not k:
            return 0
        l = 0 
        r = 0
        d = {}
        max_l = 1
        
        while r < len(s):
            if s[r] in d:
                d[s[r]] += 1
            if not s[r] in d:
                d[s[r]] = 1
            
            is_valid = (len(d) <= k)
            
            if not is_valid:
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del d[s[l]]
                l += 1
                
            max_l = max(max_l, r-l+1)
            r += 1
        return max_l
                
            
        