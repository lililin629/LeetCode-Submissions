class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = r = 0
        d = defaultdict(int)
        
        while r < len(nums):
            d[nums[r]] += 1
            if r - l > k:
                d[nums[l]] -= 1
                l += 1
            if d[nums[r]] > 1:
                return True
            r += 1
        
        return False
            
            
        