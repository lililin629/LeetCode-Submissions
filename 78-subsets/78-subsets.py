class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        if not nums:
            return subsets
        self.dfs(sorted(nums), 0, [], subsets)
        return subsets
        
    
    def dfs(self, nums, index, subset, subsets):
        subsets.append(list(subset))
        
        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i+1, subset, subsets)
            subset.pop()
            
        
#     def dfs(self, nums, index, subset, subsets):
#         if index == len(nums):
#             subsets.append(list(subset))
#             return
        
#         # chosen
#         subset.append(nums[index])
#         self.dfs(nums, index+1, subset, subsets)
#         # not chosen
#         subset.pop()
#         self.dfs(nums, index+1, subset, subsets)
        
        