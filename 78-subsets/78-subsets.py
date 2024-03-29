class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        if not nums:
            return subsets
        self.dfs(sorted(nums), 0, [], subsets)
        return subsets
        
    
    def dfs(self, nums, index, subset, subsets):
        if index == len(nums):
            subsets.append(list(subset))
            return
        
        # 選
        subset.append(nums[index])
        self.dfs(nums, index+1, subset, subsets)
        # 不選
        subset.pop()
        self.dfs(nums, index+1, subset, subsets)


        