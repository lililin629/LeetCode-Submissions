class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = defaultdict(bool)
        dp[-1] = True
        
        for i in range(n):
            for word in wordDict:
                l = len(word)
                if dp[i-l] and s[i-l+1:i+1] == word:
                    dp[i] = True
        return dp[n-1]
                
        