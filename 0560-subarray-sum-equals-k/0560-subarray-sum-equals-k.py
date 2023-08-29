class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        d = defaultdict(int)
        prefix_sum = 0
        d[prefix_sum] += 1
        ans = 0
        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in d:
                ans += d[prefix_sum - k]
            d[prefix_sum] += 1
       
        return ans
            
            
            
        