# (Sum - prev_sum)%k = ck%k
# sum%k - prev_sum%k = 0
# sum%k = prev_sum%k
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = defaultdict(int)
        d[0] = -1
        s = 0
        
        for i in range(len(nums)):
            
            s += nums[i]
            if s % k not in d:
                d[s%k] = i
            elif d[s%k] < i-1:
                return True
        return False
            
            
            
        