class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # l = len(s)-1
        # if dp[n-1] and s[n:k]: dp[k] = 1
        
        wordSet = set(wordDict)  # Use a set for faster lookups
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Empty string is always valid

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[len(s)]
        