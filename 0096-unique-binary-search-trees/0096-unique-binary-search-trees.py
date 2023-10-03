class Solution:
    def numTrees(self, n: int) -> int:
        return self.helper(1, n)
    
    @cache
    def helper(self, start, end):
        if start > end:
            return 1
        if start == end:
            return 1
        
        num = 0
        for i in range(start, end+1):
            l = self.helper(start,i-1)
            r = self.helper(i+1,end)
            num += l*r
        return num
            
        