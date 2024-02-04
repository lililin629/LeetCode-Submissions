class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        d1 = defaultdict(int)
        d2 = defaultdict(list)
        
        for [c, pr] in prerequisites:
            d1[c] += 1
            d2[pr].append(c)
        
        q = deque()
        taken = set()
        
        for c in range(numCourses):
            if c not in d1:
                q.append(c)
                taken.add(c)
        
        while q:
            cur_c = q.popleft()
        
            for next_c in d2[cur_c]:
                d1[next_c] -= 1
                if d1[next_c] == 0 and next_c not in taken:
                    q.append(next_c)
                    taken.add(next_c)

                    if len(taken) == numCourses:
                        return True
        return False
            
            
                