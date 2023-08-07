class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output
#         self.ans = []
        
#         for l in range(len(nums)+1):
#             self.dfs(l, 0, nums, [])
#         return self.ans
        
    
#     def dfs(self, l, pointer, nums, cur):
#         if len(cur) == l:
#             self.ans.append(list(cur))
#             return
        
#         for j in range(pointer, len(nums)):
#             cur.append(nums[j])
#             self.dfs(l, j+1, nums, cur)
#             cur.pop()
        
        