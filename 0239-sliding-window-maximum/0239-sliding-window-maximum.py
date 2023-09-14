# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         # edge case
#         if k == 1:
#             return nums
        
#         # 2 pointers
#         l = 0  #first ele of window
#         r = k  #1 ele to the rihgt of the last ele
#         cur_max = max(nums[:k])
#         d = Counter(nums[:k])
#         ans = [cur_max]
        
#         while r < len(nums):
#             # update d 
#             d[nums[r]] += 1
#             d[nums[l]] -= 1
#             if d[nums[l]] == 0:
#                 del d[nums[l]]
#             # update cur_max
#             if nums[r] > cur_max:
#                 cur_max = nums[r]
#             else:
#                 if cur_max not in d:
#                     cur_max = max(d)
#             ans.append(cur_max) 
            
#             # move window to the right
#             l += 1
#             r += 1
        
#         return ans        


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        # Deque to store elements in decreasing order
        dq = deque()
        ans = []
        
        for i, n in enumerate(nums):
            # print(dq)
            # Remove elements that are out of this window
            if dq and i-dq[0]+1 > k:
                dq.popleft()
            
            # Remove elements that are smaller than the current element
            while dq and nums[dq[-1]] < n:
                dq.pop()
            
            dq.append(i)
           
            # The first element is the maximum element of previous window, add it to the result
            if i >= k - 1:
                
                ans.append(nums[dq[0]])
        
        return ans

            
            
            
            
        