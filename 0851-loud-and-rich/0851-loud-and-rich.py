class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        g = defaultdict(list)
        ind = [0]*n
        for [r, p] in richer:
            g[r].append(p)
            ind[p] += 1
        # print(g)
        ans = [i for i in range(n)]
        
        q = deque()
        for i in range(n):
            if ind[i] == 0:
                q.append(i)
                ans[i] = i
                
        while q:
            node = q.popleft()
            for poor in g[node]:
                ind[poor] -= 1
                if quiet[ans[node]] < quiet[ans[poor]]:
                    ans[poor] = ans[node]
                if ind[poor] == 0:
                    q.append(poor)
        return ans
            
            
        
        