class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # base case
        if not nums:
            return [[]]
        # divide
        ans = []
        for lst in self.subsets(nums[1:]):
            ans.append(lst)
            ans.append(lst + [nums[0]])      # make a new lst, do not mutate lst
        return ans
            
        