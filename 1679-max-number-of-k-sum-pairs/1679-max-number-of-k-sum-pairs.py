class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        d = Counter(nums)
        count = 0
        for num in d:
            if k-num in d:
                if k-num == num:
                    count += d[num]//2
                    d[num] = 0
                else:
                    count += min(d[num], d[k-num])
                    d[num] = 0
        return count
                    
        
        
        
        
        
        

            
        