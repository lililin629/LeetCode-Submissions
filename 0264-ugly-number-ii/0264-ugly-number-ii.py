import heapq

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.heap = [1]
        heapq.heapify(self.heap)
        self.set = {1}
        
        for i in range(n-1):
            ugly_num = heapq.heappop(self.heap)
            for factor in [2,3,5]:
                new_ugly = ugly_num*factor
                if new_ugly not in self.set:
                    self.set.add(new_ugly)
                    heapq.heappush(self.heap, new_ugly)
        ugly_num = heapq.heappop(self.heap)
        return ugly_num
    
            
        