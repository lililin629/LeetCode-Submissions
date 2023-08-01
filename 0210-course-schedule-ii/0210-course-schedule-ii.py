class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degrees = [0]*numCourses
        d = defaultdict(list)
        ans = []

        for target, pre in prerequisites: 
            d[pre].append(target)
            in_degrees[target] += 1
        
        q = deque()
        for i in range(numCourses):
            if in_degrees[i] == 0:
                q.append(i)
        
        while q:
            c = q.popleft()
            ans.append(c)
            for t in d[c]:
                in_degrees[t] -= 1
                if in_degrees[t] == 0:
                    q.append(t)
        if len(ans) < numCourses:
            return []
        return ans
        
        