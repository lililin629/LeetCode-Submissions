#         nums2 = [-1*ele for ele in nums]
#         heapq.heapify(nums2)
        
#         for _ in range(k):
#             ans = heapq.heappop(nums2)
            
#         return -1*ans
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        return self.partition(0, n-1, n-k, nums) # n-k is the 0-based index of the kth largest number
        
    def partition(self, start, end, k, nums):
        # partition
        # invariant: start <= k <= end
        if start == end:
            return nums[k]
        
        l, r = start, end
        mid = (l+r)//2
        piv = nums[mid]
        while l <= r:
            while l <= r and nums[r] > piv:
                r -= 1
            while l <= r and nums[l] < piv:
                l += 1
            if l <= r:
                nums[r],  nums[l] = nums[l], nums[r]
                l += 1
                r -= 1
        
        if r >= k:
            return self.partition(start, r, k, nums)
        if l <= k:
            return self.partition(l, end, k, nums)
        return nums[k]
        
        