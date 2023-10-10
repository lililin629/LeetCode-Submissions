class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        l = self.sortArray(nums[:mid])
        r = self.sortArray(nums[mid:])
        return self.merge(l, r)
    
    def merge(self, l, r):
        p1 = p2 = 0
        ret = []
        while p1 < len(l) and p2 < len(r):
            if l[p1] <= r[p2]:
                ret.append(l[p1])
                p1 += 1
            else:
                ret.append(r[p2])
                p2 += 1
        ret.extend(l[p1:])
        ret.extend(r[p2:])
        return ret
                
            
        