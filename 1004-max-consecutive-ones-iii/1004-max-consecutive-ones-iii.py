class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        ret = 0
        while r < len(nums):
            if nums[r] == 1:
                r += 1
                ret = max(ret, r-l)
                
            else:
                if k > 0:
                    r += 1
                    k -= 1
                    ret = max(ret, r-l)
                else:
                    while k <= 0:
                        if nums[l] == 0:
                            k += 1
                        l += 1         
        return ret
                            
                        
                    
                
            
            
        