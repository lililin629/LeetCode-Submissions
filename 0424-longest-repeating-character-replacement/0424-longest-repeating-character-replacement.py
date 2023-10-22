class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        all_char = Counter(s)
        self.mx_len = 0
        
        for ch in all_char:
            self.find_len(ch, s, k)
            
        return self.mx_len
    
    def find_len(self, ch, s, k):
        l = r = 0
        d = defaultdict(int)
        while r < len(s):
            d[s[r]] += 1
            while r-l+1-d[ch] > k:
                d[s[l]] -= 1
                l += 1
              
            self.mx_len = max(self.mx_len, r-l+1)
            r += 1
           
          
                
                
            
        
        
        
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
            
#         # binary search for length
#         lo, hi = 1, len(s)
#         while lo+1 < hi:
#             mid = (lo + hi)//2
#             if self.isValid(s, mid, k):
#                 lo = mid
#             else:
#                 hi = mid
#         if self.isValid(s, hi, k):
#             return hi
#         return lo
        
#     def isValid(self, s, length, k):
#         # sliding window
#         d = defaultdict(int)
#         max_ct = 0
#         start = 0
#         for end in range(len(s)):
#             d[s[end]] += 1
#             if end + 1 - start > length:
#                 d[s[start]] -= 1
#                 start += 1
#             max_ct = max(max_ct, d[s[end]])
#             if length - max_ct <= k:
#                 return True
#         return False
        
        
        
            
                    
                
            
        