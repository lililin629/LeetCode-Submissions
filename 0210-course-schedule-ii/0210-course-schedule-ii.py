class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g1 = defaultdict(int)
        g2 = defaultdict(list)
        
        for i in range(numCourses):
            g1[i] = 0
    
        for [c, p] in prerequisites:
            g1[c] += 1
            g2[p].append(c)
        
        q = deque()
        taken = set()
        ans = []
        for c in g1:
            if g1[c] == 0:
                q.append(c)
                taken.add(c)
        # print(g1)
        # print(g2)
        # print(q)
        while q:
            cur = q.popleft()
            ans.append(cur)
            for nx in g2[cur]:
                g1[nx] -= 1
                if g1[nx] == 0 and nx not in taken:
                    q.append(nx)
                    taken.add(nx)
        if len(ans) < numCourses:
            return []
        return ans
                    
                
            
        