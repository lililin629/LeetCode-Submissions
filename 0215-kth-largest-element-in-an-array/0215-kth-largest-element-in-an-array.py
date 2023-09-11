class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums2 = [-1*ele for ele in nums]
        heapq.heapify(nums2)
        
        for _ in range(k):
            ans = heapq.heappop(nums2)
            
        return -1*ans
        