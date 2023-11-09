class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        memo = defaultdict(int)
        for i in range(l1-1, -1, -1):
           
            for j in range(l2-1, -1, -1):
                if text1[i] == text2[j]:
                    memo[(i, j)] = 1 + memo[(i+1, j+1)]
                else:
                    memo[(i, j)] = max(memo[(i+1, j)], memo[(i, j+1)])
        return memo[(0, 0)]
                
        