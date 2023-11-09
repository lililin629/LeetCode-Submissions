class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        
        while l + 1 < r:
            ml = nums[((l+r)//2)-1]
            m = nums[(l+r)//2]
            mr = nums[((l+r)//2)+1]
            if m > mr and m > ml:
                return (l+r)//2
            elif mr > m > ml:
                l = ((l+r)//2)+1
            elif mr < m < ml:
                r = ((l+r)//2)-1
            else:
                r = ((l+r)//2)-1
                
        if nums[l] > nums[r]:
            return l
        else:
            return r
            
            
            
            
        