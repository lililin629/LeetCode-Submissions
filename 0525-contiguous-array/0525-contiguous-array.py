class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        d = defaultdict(int)
        max_len = 0
        ps = 0
        d[ps] = -1
        
        for i in range(len(nums)):
            ps += nums[i]
            if ps in d:
                max_len = max(max_len, i-d[ps])
            else:
                d[ps] = i
        return max_len
                
        
        
    
        