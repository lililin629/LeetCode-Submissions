class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)
        
        l = r = 0
        ans = 0
        
        while r < len(s):
            d[s[r]] += 1
            
            # invariant: every char in the window must not have duplicates
            while d[s[r]] > 1:
                d[s[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)
            r += 1
        return ans
            
                