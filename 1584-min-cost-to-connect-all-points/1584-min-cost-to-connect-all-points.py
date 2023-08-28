class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [float('inf')]*n
        dist[0] = 0
        
        linked = set()
        ans = 0
        # heap = [(dist[0], 0)]
        # heapq.heapify(heap)
        
        while len(linked) < n+1:
            # cur = heapq.heappop(heap)
            mind = float('inf')
            cur = -1
            for i, d in enumerate(dist):
                if i not in linked and d < mind:
                    mind = d
                    cur = i
                    ans += mind
            [curx, cury] = points[cur]
            linked.add(cur)
            for i in range(n):
                if i not in linked:
                    [xi, yi] = points[i]
                    dist[i] = min(dist[i], abs(curx-xi)+abs(cury-yi))
                    # heapq.heappush(heap, (dist[i], i))
        print(dist)
        return sum(dist)
                    
            
        
        