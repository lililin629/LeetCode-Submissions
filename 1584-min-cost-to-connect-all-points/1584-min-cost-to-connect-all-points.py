class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [float('inf')]*n
        dist[0] = 0
        linked = set([0])
       
        self.update_dist(n, points, dist, points[0][0], points[0][1], linked)
        while len(linked) < n:
            mind = float('inf')
            cur = -1
            for i, d in enumerate(dist):
                if i not in linked and d < mind:
                    mind = d
                    cur = i
            [curx, cury] = points[cur]
            linked.add(cur)
            self.update_dist(n, points, dist, curx, cury,linked)
            # for i in range(n):
            #     if i not in linked:
            #         [xi, yi] = points[i]
            #         dist[i] = min(dist[i], abs(curx-xi)+abs(cury-yi))
        print(dist)            
        return sum(dist)
    
    def update_dist(self, n, points, dist, curx, cury, linked):
        for i in range(n):
                if i not in linked:
                    [xi, yi] = points[i]
                    dist[i] = min(dist[i], abs(curx-xi)+abs(cury-yi))
        
                    
            
        
        