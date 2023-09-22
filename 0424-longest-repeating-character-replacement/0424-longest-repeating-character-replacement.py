class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
            
        # binary search for length
        start, end = 1, len(s)+1
        while start+1 < end:
            mid = start + (end-start)//2
            if self.isValid(s, mid, k):
                start = mid
            else:
                end = mid
        return start
        
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
        
        
        
            
                    
                
            
        