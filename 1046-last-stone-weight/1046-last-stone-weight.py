class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones2 = [-1*s for s in stones]
        heapq.heapify(stones2)
        
        while len(stones2) > 1:
            x = -1*heapq.heappop(stones2)
            y = -1*heapq.heappop(stones2)
            if x != y:
                heapq.heappush(stones2, -1*(x-y))
        return -1*stones2[0] if stones2 else 0
                
            
        