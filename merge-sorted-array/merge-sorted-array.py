class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ans = []
        l = r = 0
        if n == 0:
            return
        elif m == 0:
            nums1[:] = nums2[:]
        else:
            while l < m and r < n:
                if nums1[l] <= nums2[r]:
                    ans.append(nums1[l])
                    l += 1
                else:
                    ans.append(nums2[r])
                    r += 1
            if l < m:
                ans.extend(nums1[l:])
            if r < n:
                ans.extend(nums2[r:])
                
            for i in range(m+n):
                nums1[i] = ans[i]
            
            
            