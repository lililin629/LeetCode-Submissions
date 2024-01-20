class Solution:
    def partition(self, s: str) -> List[List[str]]:
        d = defaultdict(int)
        
        for i in range(len(s)):
            d[(i, i)] = 1
            
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                d[(i-1, i)] = 1
        
        for length in range(2, len(s)):
            for start in range(0, len(s)-length):
                end = start + length
                if s[start] == s[end] and d[(start+1, end-1)]:
                    d[(start, end)] = 1
        ans = []
        n = len(s)
        self.dfs(d, s, 0, n, [], ans)
        return ans
        
    def dfs(self, d, s, start, n, cur, ans):
        if start == n:
            ans.append(list(cur))
            return
        for end in range(start, n):
            if d[(start,end)]:
                cur.append(s[start:end+1])
                self.dfs(d,s,end+1,n,cur,ans)
                cur.pop()
            
            
            
            
            
        