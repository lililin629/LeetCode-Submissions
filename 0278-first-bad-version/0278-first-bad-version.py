# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.helper(1, n)
    
    def helper(self, start, end):
        
        mid = (start + end)//2
        if isBadVersion(mid) and not isBadVersion(mid-1):
            return mid
        elif isBadVersion(mid) and isBadVersion(mid-1):
            return self.helper(start, mid-1)
        else:
            return self.helper(mid+1, end)
            
            
        