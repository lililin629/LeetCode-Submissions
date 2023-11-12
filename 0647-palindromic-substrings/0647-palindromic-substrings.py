class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0 
        memo = defaultdict(bool)
        for i in range(len(s)):
            memo[(i, i)] = True
            ans += 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                memo[(i-1, i)] = True
                ans += 1
              
        for length in range(2, len(s)):
            for i in range(len(s) - length):
                j = i + length
                if s[i] == s[j] and memo[(i + 1, j - 1)]:
                    memo[(i, j)] = True
                    ans += 1
                
        return ans
                
                    
                
        