class Solution:
    def longestPalindrome(self, s: str) -> int:
        has_extra = False
        ans = 0
        ch_map = dict()
        for ch in s:
            if ch not in ch_map:
                ch_map[ch] = 1
            else:
                ch_map[ch] += 1
        
        for ch in ch_map:
            if ch_map[ch] % 2 == 0:
                ans += ch_map[ch]
            else:
                has_extra = True
                ans += (ch_map[ch] - 1)
        if has_extra:
            ans += 1
        return ans
            
            
                
                
                
        
            
            
        
        