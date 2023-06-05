import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        self.heap = []
        
        for point in points:
            dist = (point[0])**2 + (point[1])**2
            heapq.heappush(self.heap, (-dist, point))
            if len(self.heap) > k:
                heapq.heappop(self.heap)
        
        ret = []
        while len(self.heap) > 0:
            p = heapq.heappop(self.heap)
            ret.append(p[1])
        return ret
            
               
                