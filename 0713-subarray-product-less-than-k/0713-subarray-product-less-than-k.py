class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        l = 0
        r = 0
        
        prod = 1
        count = 0
        
        while l <= r < len(nums):
            if prod == 1 and prod* nums[r] >= k:
                l += 1
                r += 1
    
            elif prod* nums[r] < k:
                prod *= nums[r]
                count += (r-l+1)
                r += 1
            else:
                prod //= nums[l]
                l += 1
        
        return count
           
        # # 10, 5, 2, 6
        #       l  r
        # # 10
        # # 10, 5
        
            
        