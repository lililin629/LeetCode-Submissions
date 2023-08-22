class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        l = len(word1)-1
        r = len(word2)-1
        return self.helper(word1, word2, l, r)
        
        
    @cache
    def helper(self, word1, word2, l, r):
        if l < 0:
            return r + 1
        if r < 0:
            return l + 1
            
        if word1[l] == word2[r]:
            return self.helper(word1, word2, l-1, r-1)
        
        
        d = 1 + self.helper(word1, word2, l, r-1)
        i = 1 + self.helper(word1, word2, l-1, r)
        r = 1 + self.helper(word1, word2, l-1, r-1)
        return min(d, i, r)
        