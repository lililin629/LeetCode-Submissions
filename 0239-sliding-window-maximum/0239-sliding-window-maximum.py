class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # edge case
        if k == 1:
            return nums
        
        # 2 pointers
        l = 0  #first ele of window
        r = k  #1 ele to the rihgt of the last ele
        cur_max = max(nums[:k])
        d = Counter(nums[:k])
        ans = [cur_max]
        
        while r < len(nums):
            d[nums[r]] += 1
            d[nums[l]] -= 1
            if d[nums[l]] == 0:
                del d[nums[l]]
            if nums[r] > cur_max:
                cur_max = nums[r]
            else:
                if cur_max not in d:
                    cur_max = max(d)
            ans.append(cur_max) 
            l += 1
            r += 1
        
        return ans        
            
            
            
            
            
        