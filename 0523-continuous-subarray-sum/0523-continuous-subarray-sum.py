class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(1, len(nums)):
            if nums[i-1]%k == 0 and nums[i]%k == 0:
                return True
        s = set()
        s.add(0)
        prefix_sum = 0
        ps1 = 0
        
        for i in range(len(nums)):
            prefix_sum += nums[i]
            ps1 = prefix_sum % k
            
            
            if nums[i] % k == 0:
                continue
                
          
            if ps1 in s:
                return True
            s.add(ps1)
            
        return False
            
            
            
        