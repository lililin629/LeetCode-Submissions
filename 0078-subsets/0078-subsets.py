class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        k = len(nums)-1
        return self.dfs(k, nums)
    
    
    def dfs(self, k, nums):
        if k < 0:
            return [[]]
        pre = self.dfs(k-1, nums)
        ans = []
        for ls in pre:
            ans.append(ls+[nums[k]])
        return pre+ans
        
        
       
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
        
        