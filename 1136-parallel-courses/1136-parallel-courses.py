class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        degrees = [0]*(n+1)
        graph = defaultdict(list)
        
        for [pre, nex] in relations:
            graph[pre].append(nex)
            degrees[nex] += 1
        
        start = []
        for i in range(1, n+1):
            if degrees[i] == 0:
                start.append(i)
                
            
        q = deque(start)
        sem = 0
        taken = set()
        
        while q:
            sem += 1
            l = len(q)
            for i in range(l):
                cur = q.popleft()
                taken.add(cur)
                for nex in graph[cur]:
                    if nex not in taken:
                        degrees[nex] -= 1
                        if degrees[nex] == 0:
                            q.append(nex)
        
        if len(taken) != n:
            return -1
        return sem
        