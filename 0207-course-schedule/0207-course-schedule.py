class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological: 可以修就修
        
        ind = [0]*numCourses
        d = defaultdict(list)
        
        for c, p in prerequisites:
            d[p].append(c)
            ind[c] += 1
        
        q = deque([i for i in range(numCourses) if ind[i] == 0])
        sched = []
        
        while q:
            c1 = q.popleft()
            sched.append(c1)
            for c2 in d[c1]:
                ind[c2] -= 1
                if ind[c2] == 0:
                    q.append(c2)
        
        if len(sched) == numCourses:
            return True
        return False
            
            
        