class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        b = 0
        e = len(nums)-1
        while b < e:
            m = (b+e)//2
            if nums[m] == nums[m-1]:
                if (m-1-b) % 2 == 0:
                    b = m + 1
                else:
                    e = m - 2
            elif nums[m] == nums[m+1]:
                if (m-b) % 2 == 0:
                    b = m + 2
                else:
                    e = m - 1
            else:
                return nums[m]
        return nums[b]
            
        
        
####################################Brute Force######################################
#         if len(nums) == 1:
#             return nums[0]
#         else:
#             f = 0
#             s = 1
#             while s < len(nums):
#                 if nums[f] == nums[s]:
#                     f += 2
#                     s += 2
#                 else:
#                     return nums[f]
#             return nums[f]
                
        