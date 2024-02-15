class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ps = 0
        d = defaultdict(int)
        
        for i, num in enumerate(nums):
            ps += num
            d[i] = ps
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < d[i-1]:
                return d[i]
        return -1
        
        
            
        