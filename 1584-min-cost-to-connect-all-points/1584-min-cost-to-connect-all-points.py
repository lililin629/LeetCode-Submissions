class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        dist = [float('inf')]*n
        dist[0] = 0
        heap = []
        for i, d in enumerate(dist):
            heap.append((d, i))

        linked = set()
        # total = 0
        
       
        while heap:
            # print(heap)
            cur_dist, cur = heapq.heappop(heap)
            if cur not in linked:
                linked.add(cur)
                # total += cur_dist
                # print(f"{cur_dist}, {cur}")
                # print(linked)

                for i in range(n):
                    if i not in linked:
                        if self.calc_dist(cur, i, points) < dist[i]:
                            dist[i] = self.calc_dist(cur, i, points)
                            heapq.heappush(heap, (dist[i], i))
                        
        return sum(dist)
    
    def calc_dist(self, start, end, points):
        [sx, sy] = points[start]
        [ex, ey] = points[end]
        return abs(sx-ex) + abs(sy-ey)

    
    
# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         n = len(points)
        
#         dist = [self.calc_dist(0, i, points) for i in range(n)]
#         linked = set([0])
       
#         while len(linked) < n:
#             mind = float('inf')
#             cur = -1
#             for i, d in enumerate(dist):
#                 if i not in linked and d < mind:
#                     mind = d
#                     cur = i
#             [curx, cury] = points[cur]
#             linked.add(cur)

#             for i in range(n):
#                 if i not in linked:
#                     dist[i] = min(dist[i], self.calc_dist(cur, i, points))
               
#         return sum(dist)
    
#     def calc_dist(self, start, end, points):
#         [sx, sy] = points[start]
#         [ex, ey] = points[end]
#         return abs(sx-ex) + abs(sy-ey)                    
            
        
        