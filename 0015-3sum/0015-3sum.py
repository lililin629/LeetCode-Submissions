# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         ans = []
        
#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 break
#             if  i != 0 and nums[i - 1] == nums[i]:
#                 continue
            
            
#             target = -nums[i]
#             f = i+1
#             e = len(nums)-1
#             while f < e:
#                 if nums[f]+nums[e] == target:
#                     ans.append([nums[i], nums[f], nums[e]])
#                     f += 1
#                     e -= 1
#                     while f < e and nums[f] == nums[f-1]:
#                         f += 1
                    
#                 if nums[f]+nums[e] < target:
#                     f += 1
#                 else:
#                     e -= 1
#         return ans
                    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1            
                    
            
            
            
        