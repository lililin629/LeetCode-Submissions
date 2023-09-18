class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # n = len(nums)
        # new = [int(num) for num in nums]
        # heapq.heapify(new)
        # for i in range(n-k+1):
        #     cur = heapq.heappop(new)
        # return str(cur)
        ############################################################
        #######################Quick Select#########################
        
        n = len(nums)
        new = [int(num) for num in nums]
        
        return self.qs(0, n-1, new, n-k)
        
    def qs(self, start, end, new, k):
        
        if start == end:
            return str(new[k])
        l, r = start, end
        piv = new[(start+end)//2]
        
        while l <= r:
            while l <= r and new[r] > piv:
                r -= 1
            while l <= r and new[l] < piv:
                l += 1
            if l <= r:
                new[r], new[l] =  new[l], new[r]
                l += 1
                r -= 1
        
        if k <= r:
            return self.qs(start, r, new, k)
        if k >= l:
            return self.qs(l, end, new, k)
        return str(new[k])
        
            
                
        
    
        
        
        
        
        