class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find first dip
        n = len(nums)
        left = -1
        for i in range(n-1, 0, -1):
            if nums[i-1] < nums[i]:
                left = i-1
                break
        print(left)
        print(nums[left])
        # swap
        right = n-1
        if left != -1:
            for j in range(left+1, n):
                if nums[j] <= nums[left]:
                    right = j-1
                    break
            nums[left], nums[right] = nums[right], nums[left]
       
        print(nums)             
        # reverse
        mid = (n+left)//2
        print(mid)
        for i in range(left+1, mid+1):
            nums[i], nums[n+left-i] = nums[n+left-i], nums[i]
            
        