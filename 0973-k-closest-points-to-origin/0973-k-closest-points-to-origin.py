class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(self.dist(point), point) for point in points]
        heapq.heapify(heap)
        ans = []
        
        for _ in range(k):
            p = heapq.heappop(heap)
            ans.append(p[1])
        return ans
        
    def dist(self, point):
        [x, y] = point
        return x**2 + y**2
        