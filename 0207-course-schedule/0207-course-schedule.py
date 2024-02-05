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
        num_taken = 0
      
        for c in range(numCourses):
            if c not in d1:
                q.append(c)
               
        while q:
            cur_c = q.popleft()
            num_taken += 1
            if num_taken == numCourses:
                return True
        
            for next_c in d2[cur_c]:
                d1[next_c] -= 1
                if d1[next_c] == 0:
                    q.append(next_c)
                
        return False
            
            
                