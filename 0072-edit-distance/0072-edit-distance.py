class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        l = len(word1)-1
        r = len(word2)-1
        self.dp = [ [-1]*(r+1) for _ in range(l+1) ]
        
        return self.helper(word1, word2, l, r)
        
        
    
    def helper(self, word1, word2, l, r):
        
        if l == -1:
            return r+1
        if r == -1:
            return l+1
        
        if self.dp[l][r] != -1:
            return self.dp[l][r]
        
        if word1[l] == word2[r]:
            self.dp[l][r] = self.helper(word1, word2, l-1, r-1)
            return self.dp[l][r]
       
        
        d = 1 + self.helper(word1, word2, l, r-1)
        i = 1 + self.helper(word1, word2, l-1, r)
        re = 1 + self.helper(word1, word2, l-1, r-1)
        self.dp[l][r] = min(d, i, re)
        return self.dp[l][r]
        