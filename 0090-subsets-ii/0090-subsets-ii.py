class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()  # Sort the input list
#         ans = []
#         self.helper(0, nums, [], ans)
#         return ans
    
#     def helper(self, start, nums, cur, ans):
#         ans.append(list(cur))
#         for i in range(start, len(nums)):
#             # Skip duplicates
#             if i > start and nums[i] == nums[i - 1]:
#                 continue
#             cur.append(nums[i])
#             self.helper(i + 1, nums, cur, ans)
#             cur.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for length in range(len(nums)+1):
            self.helper(0, nums, [], ans, length)
        return ans
    
    def helper(self, start, nums, cur, ans, length):
        if len(cur) == length:
            ans.append(list(cur))
        
        for i in range(start, len(nums)):
            if i != start and nums[i] == nums[i-1]:
                continue
            cur.append(nums[i])
            self.helper(i+1, nums, cur, ans, length)
            cur.pop()
            
        
        
        
        
   
        