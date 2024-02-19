class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        d = Counter(nums)
        count = 0
        for num in d:
            if d[num]:
                if num-k in d:
                    count += d[num]*d[num-k]
                if num+k in d:
                    count += d[num]*d[num+k]
                d[num] = 0
        return count
                
                
            
                
                
        