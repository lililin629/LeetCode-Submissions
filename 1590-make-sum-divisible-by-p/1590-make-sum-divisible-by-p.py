class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        d = defaultdict(int)
        ps = 0
        d[ps] = -1
        min_l = len(nums)
        target = sum(nums)%p
        if target == 0:
            return 0
        
        for i, num in enumerate(nums):
            ps = (ps+num)%p
            d[ps] = i
            needed = (ps - target) % p
            if needed in d:
                min_l = min(min_l, i - d[needed])
        if min_l == len(nums):
            return -1
        return min_l
            
        
        
        
        