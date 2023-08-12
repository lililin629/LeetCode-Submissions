class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        r = 0
        
        total = 0
        count = 0
        
        for r, num in enumerate(arr):
            total += num
            
            if r-l+1 == k:
                if (total // k) >= threshold:
                    count += 1
                total -= arr[l]
                l += 1
        return count
            
            
            
        