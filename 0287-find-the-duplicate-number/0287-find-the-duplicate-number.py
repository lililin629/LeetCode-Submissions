class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = 1
        e = len(nums)-1
        ans = 0

        while s <= e:
            mid = (s + e)//2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                ans = mid
                e = mid - 1
            else:
                s = mid + 1
            # s = 1, e = 2
        return ans
