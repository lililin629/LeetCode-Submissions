class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for [u, v, w] in times:
            g[u].append((w, v))
            
        dist = [float('inf')]*(n+1)
        dist[0] = 0
        dist[k] = 0
        pq = [(0, k)]
        
        while pq:
            cur_w, cur = heapq.heappop(pq)
            for weight, node in g[cur]:
                new_w = cur_w + weight
                if new_w < dist[node]:
                    dist[node] = new_w
                    # heapq.heappush(pq, (new_w, node))
                    pq.append((new_w, node))
        mx_time = max(dist)
        if mx_time == float('inf'):
            return -1
        return mx_time
                
            
        
        