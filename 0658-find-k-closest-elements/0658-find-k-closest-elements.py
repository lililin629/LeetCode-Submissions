class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff_h = []
        heapq.heapify(diff_h)
        ele_h = []
        heapq.heapify(ele_h)
        for ele in arr:
            heapq.heappush(diff_h, (abs(ele-x), ele))
        for _ in range(k):
            dist, el = heapq.heappop(diff_h)
            heapq.heappush(ele_h, el)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(ele_h))
        return ans
            
            
            
        
        
        
        
        
        