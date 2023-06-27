class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans_set = set()
        ans = []

        if not nums:
            return [[]]
        
        for x in self.subsetsWithDup(nums[1:]):
            #不選
            t = tuple(sorted(x))
            if t not in ans_set:
                ans_set.add(t)
                ans.append(x)
                
            #選nums[0]    
            x1 = list(x)
            x1.append(nums[0])
            t1 = tuple(sorted(x1))
            if t1 not in ans_set:
                ans_set.add(t1)
                ans.append(x1)
        
        return ans

