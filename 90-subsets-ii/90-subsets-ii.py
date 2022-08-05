class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        if not nums:
            return subsets
        self.dfs(sorted(nums), 0, [], subsets)
        return subsets
        
    
    def dfs(self, nums, index, subset, subsets):
        subsets.append(list(subset))  
       
        for i in range(index, len(nums)):
	    # 避免前面的2'沒選 但選了後面的2''
            if (i > index) and (nums[i] == nums[i-1]):
                continue
            subset.append(nums[i])
            self.dfs(nums, i+1, subset, subsets)
            subset.pop()

