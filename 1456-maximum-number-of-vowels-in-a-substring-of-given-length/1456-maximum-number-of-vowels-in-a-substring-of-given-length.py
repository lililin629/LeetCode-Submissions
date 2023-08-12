class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vset = {'a', 'e', 'i', 'o', 'u'}
        max_count = 0
        count = 0
        
        l = 0
        
        for r, ch in enumerate(s):
            if ch in vset:
                count += 1
                max_count = max(max_count, count)
            if r-l+1 == k:
                if s[l] in vset:
                    count -= 1
                l += 1
        return max_count
                
                
                
            
        