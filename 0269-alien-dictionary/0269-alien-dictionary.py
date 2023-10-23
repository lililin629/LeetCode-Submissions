class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = defaultdict(list)
        in_degree = defaultdict(int)
        for i in range(len(words)):
            for j in range(len(words[i])):
                in_degree[words[i][j]] = 0
            
        for i in range(len(words)-1):
            if len(words[i]) > len(words[i+1]) and words[i][:len(words[i+1])] == words[i+1]:
                return ''
            r = min(len(words[i]), len(words[i+1]))
            for j in range(r):
                if words[i][j] != words[i+1][j]:
                    g[words[i][j]].append(words[i+1][j])
                    in_degree[words[i+1][j]] += 1
                    break
        
        ans = ''
        q = deque()
        for ch in in_degree:
            if in_degree[ch] == 0:
                q.append(ch)
        while q:
            node = q.popleft()
            ans += node
            for c in g[node]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    q.append(c)
        if len(ans) != len(g):
            return ''
        return ans
            
                
            
        
        
        
            
            
        