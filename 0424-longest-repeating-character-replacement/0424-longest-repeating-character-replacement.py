class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
            
        # binary search for length
        lo, hi = 1, len(s)
        while lo+1 < hi:
            mid = (lo + hi)//2
            if self.isValid(s, mid, k):
                lo = mid
            else:
                hi = mid
        if self.isValid(s, hi, k):
            return hi
        return lo
        
    def isValid(self, s, length, k):
        # sliding window
        d = defaultdict(int)
        max_ct = 0
        start = 0
        for end in range(len(s)):
            d[s[end]] += 1
            if end + 1 - start > length:
                d[s[start]] -= 1
                start += 1
            max_ct = max(max_ct, d[s[end]])
            if length - max_ct <= k:
                return True
        return False
        
        
        
            
                    
                
            
        