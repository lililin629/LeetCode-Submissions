class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix1 = 1
        prefix2 = 1
        
        d_front = defaultdict(int)
        d_back = defaultdict(int)
        d_front[-1] = 1
        d_back[len(nums)] = 1
        
        ans = [1]*len(nums)
        
        for i in range(len(nums)):
            prefix1 *= nums[i]
            d_front[i] = prefix1
        
        for i in range(len(nums)-1, -1, -1):
            prefix2 *= nums[i]
            d_back[i] = prefix2
            
        for i in range(len(nums)):
            ans[i] = d_front[i-1]*d_back[i+1]
        
        return ans
            
            
            
            
        
            
        
        