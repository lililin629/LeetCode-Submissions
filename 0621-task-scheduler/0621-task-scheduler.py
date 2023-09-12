class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        d = defaultdict(int)
        for t in tasks:
            d[t] -= 1
        
        heap = [(count, task) for task,count in d.items()]
        heap2 = []
        heapq.heapify(heap)
        heapq.heapify(heap2)
        time = 0
        
        while heap:
            
            time += 1
            c, t = heapq.heappop(heap)
            c += 1
            if c < 0:
                heapq.heappush(heap2, (c, t))
            for i in range(n):
                if not heap and not heap2:
                    return time
                if heap:
                    nc, nt = heapq.heappop(heap)
                    nc += 1
                    if nc < 0:
                        heapq.heappush(heap2, (nc, nt))
                time += 1
            
            heap.extend(heap2)
            heap2 = []
            
        return time
                
            
            
            
        
        
        
        
            
        