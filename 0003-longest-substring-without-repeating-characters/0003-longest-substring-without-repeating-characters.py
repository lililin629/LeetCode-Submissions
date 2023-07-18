class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        dic = {s[0]: 1,}
        l = 0
        r = 1
        max_l = 1
        while r <= len(s)-1:

            if s[r] not in dic or dic[s[r]] == 0:
                dic[s[r]] = 1
                r += 1
                max_l = max(max_l, r - l)
                
            else:
                dic[s[l]] -= 1
                l += 1
        return max_l
        