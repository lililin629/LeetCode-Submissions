# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         max_sum = [0]
#         self.helper(nums, 0, '', set(), max_sum)
#         return str(max_sum[0])
    
#     def helper(self, nums, idx, cur, visited, max_sum):
#         if idx == len(nums):
#             max_sum[0] = max(max_sum[0], int(cur))
#             return
        
#         for num in nums:
#             if num in visited:
#                 continue
#             visited.add(num)
#             self.helper(nums, idx+1, cur+str(num), visited, max_sum)
#             visited.remove(num)
class Solution:
    def largestNumber(self, nums):
        nums = [str(num) for num in nums]
        nums.sort(key=lambda x: x*10, reverse=True)
        result = ''.join(nums)
        return str(int(result)) 
            
            
            
        