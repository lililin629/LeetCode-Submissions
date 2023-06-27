class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans_set = set()

        if not nums:
            return [[]]
        
        ans = []
        
        for x in self.subsetsWithDup(nums[1:]):
            x_t = tuple(sorted(x))
            if x_t not in ans_set:
                ans_set.add(x_t)
                ans.append(x)
            x1 = list(x)
            x1.append(nums[0])
            t1 = tuple(sorted(x1))
            if t1 not in ans_set:
                ans_set.add(t1)
                ans.append(x1)
        
        return ans

