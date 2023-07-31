class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0 
        d = {}
        max_l = 1
        max_freq = 0

        while r < len(s):
            if s[r] in d:
                d[s[r]] += 1
            if s[r] not in d:
                d[s[r]] = 1
            
            max_freq = max(max_freq, d[s[r]])
            is_valid = ((r - l + 1 - max_freq) <= k) # 需要改 <= 可改

            if not is_valid:
                d[s[l]] -= 1
                l += 1
            
            max_l = max(max_l, r - l + 1)
            
            r += 1
        
        return max_l
                


            

       