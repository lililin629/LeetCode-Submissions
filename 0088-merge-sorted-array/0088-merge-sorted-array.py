class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        my_h = []
        for n in nums1[:m]:
            heapq.heappush(my_h, n)
        
        for n in nums2:
            heapq.heappush(my_h, n)
        
        i = 0
        while len(my_h):
            nums1[i] = heapq.heappop(my_h)
            i += 1