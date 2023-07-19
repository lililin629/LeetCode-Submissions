class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        r = 1
        visited = {s[0]:1,}
        count = 1
        while r < len(s):
            if s[r] not in visited or visited[s[r]] == 0:
                visited[s[r]] = 1
                r += 1
                count = max(count, r-l)
            else:
                visited[s[l]] -= 1
                l += 1
        return count
        
                
                
            