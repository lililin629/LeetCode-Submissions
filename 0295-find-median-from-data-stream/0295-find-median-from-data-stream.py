class MedianFinder:

    def __init__(self):
        self.min_h = [] # larger nums
        self.max_h = [] # smaller nums
        

    def addNum(self, num: int) -> None:
       # len(min_h) >= len(max_h)
        if len(self.min_h) == len(self.max_h):
            heapq.heappush(self.max_h, -num)
            heapq.heappush(self.min_h, -heapq.heappop(self.max_h))
        if len(self.min_h) > len(self.max_h):
            heapq.heappush(self.min_h, num)
            heapq.heappush(self.max_h, -heapq.heappop(self.min_h))       
        
        

    def findMedian(self) -> float:
        
        
        if len(self.min_h) > len(self.max_h):
            return self.min_h[0]
        else:
            return (self.min_h[0] - self.max_h[0])/2
       
       
        
        
        
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()