class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        if m < n:
            return -1
        starts = []
        for i, c in enumerate(haystack):
            if c == needle[0]:
                if m-i >= n:
                    starts.append(i)
        for i in starts:
            for j in range(n):
                if haystack[i+j] != needle[j]:
                    break
                if haystack[i+j] == needle[j] and j == n-1:
                    return i
        return -1
        
        
        