class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff_h = []
        heapq.heapify(diff_h)
        for ele in arr:
            heapq.heappush(diff_h, (abs(ele-x), ele))
        ans = []
        for _ in range(k):
            dist, el = heapq.heappop(diff_h)
            ans.append(el)
        ans.sort()
        return ans
            
       
            
            
        
        
        
        
        
        