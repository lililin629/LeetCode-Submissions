class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        dist = [self.calc_dist(0, i, points) for i in range(n)]
        linked = set([0])
       
        while len(linked) < n:
            mind = float('inf')
            cur = -1
            for i, d in enumerate(dist):
                if i not in linked and d < mind:
                    mind = d
                    cur = i
            [curx, cury] = points[cur]
            linked.add(cur)

            for i in range(n):
                if i not in linked:
                    dist[i] = min(dist[i], self.calc_dist(cur, i, points))
               
        return sum(dist)
    
    def calc_dist(self, start, end, points):
        [sx, sy] = points[start]
        [ex, ey] = points[end]
        return abs(sx-ex) + abs(sy-ey)
  
                    
            
        
        