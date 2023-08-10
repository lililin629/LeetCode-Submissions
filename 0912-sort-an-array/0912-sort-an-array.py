class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums)-1)
        return nums
    
    
    def merge_sort(self, nums, start, end):
        if start >= end:
            return
        mid = (start+end)//2
        self.merge_sort(nums, start, mid)
        self.merge_sort(nums, mid+1, end)
        self.merge(nums, start, mid, end)
        
    
    def merge(self, nums, start, mid, end):
        l = nums[start:mid+1]
        r = nums[mid+1:end+1]
        
        p1 = 0
        p2 = 0
        p3 = start
        while p1 < len(l) and p2< len(r):
            if l[p1] < r[p2]:
                nums[p3] = l[p1]
                p1 += 1
            else:
                nums[p3] = r[p2]
                p2 += 1
            p3 += 1
        while p1 < len(l):
            nums[p3] = l[p1]
            p3 += 1
            p1 += 1
        while p2 < len(r):
            nums[p3] = r[p2]
            p3 += 1
            p2 += 1
        
        
            
            
        
       
        
            

        
        