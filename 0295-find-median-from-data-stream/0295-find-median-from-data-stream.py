class MedianFinder:

    def __init__(self):
        self.lst = []
        
        

    def addNum(self, num: int) -> None:
        self.lst.append(num)
        

    def findMedian(self) -> float:
        self.lst.sort()
        n = len(self.lst)
        if n % 2 != 0:
            idx = n//2
            return self.lst[idx]
        else:
            idx1 = n // 2
            idx2 = n//2 - 1
            return (self.lst[idx1] + self.lst[idx2])/2
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()