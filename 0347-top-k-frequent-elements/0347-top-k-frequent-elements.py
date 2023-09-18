class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        new = [(count, num) for num, count in d.items()]
        
        n = len(d)
        self.partition(0, n-1, new, n-k)
        return [j for i, j in new[n-k:]]

    def partition(self, start, end, new, k):
        if start == end:
            return
        l, r = start ,end
        piv = new[(l+r)//2][0]
        
        while l <= r:
            while l <= r and new[r][0] > piv:
                r -= 1
            while l <= r and new[l][0] < piv:
                l += 1
            
            if l <= r:
                new[r], new[l] = new[l], new[r]
                l += 1
                r -= 1
        # r是左邊的終點，l是右邊的起點
        if k <= r:
            self.partition(start, r, new, k)
        if k >= l:
            self.partition(l, end, new, k)
        
                
                
            