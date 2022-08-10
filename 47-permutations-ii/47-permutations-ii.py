class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        # write your code here
        permutations = []
        visited = [False]*len(nums)
        self.helper(sorted(nums), permutations, [], visited)
        return permutations
        
    def helper(self, nums, permutations, cur_lst, visited):
        if len(cur_lst) == len(nums):
            permutations.append(list(cur_lst))
            return
            
        for i in range(len(nums)):
            if visited[i]:
                continue
            if (i > 0 and nums[i] == nums[i-1] and not visited[i-1]):
                continue
            cur_lst.append(nums[i])
            visited[i] = True
            self.helper(nums, permutations, cur_lst, visited)
            cur_lst.pop()
            visited[i] = False
            
