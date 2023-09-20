class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        ps = 0
        d[ps] += 1
        ans = 0
        
        for num in nums:
            ps += num
            mod = ps%k
            if mod in d:
                ans += d[mod]
            d[mod] += 1
        
        return ans
                    
        