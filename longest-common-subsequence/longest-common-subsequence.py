class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.memo = defaultdict(int)
        return self.dfs(text1, text2, 0, 0)
    
    def dfs(self, t1, t2, id1, id2):
        if id1 == len(t1) or id2 == len(t2):
            return 0
        if (id1, id2) not in self.memo:
            if t1[id1] == t2[id2]:
                self.memo[(id1, id2)] = 1 + self.dfs(t1, t2, id1+1, id2+1)
            if t1[id1] != t2[id2]:
                self.memo[(id1, id2)] = max(self.dfs(t1, t2, id1+1, id2), self.dfs(t1, t2, id1, id2+1))
        return self.memo[(id1, id2)]
        
        
        