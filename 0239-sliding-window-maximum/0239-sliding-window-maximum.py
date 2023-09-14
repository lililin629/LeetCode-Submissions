class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        l = 0
        r = k
        cur_max = max(nums[:k])
        
        d = defaultdict(int)
        for i in range(k):
            d[nums[i]] += 1
            
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
            
            
            
            
            
        