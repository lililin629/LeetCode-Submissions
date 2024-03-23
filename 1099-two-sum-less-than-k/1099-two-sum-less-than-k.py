class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        mx = -1
        while l < r:
            # print(nums[l])
            # print(nums[r])
            # print('---')
            summ = nums[l] + nums[r]
            if summ < k:
                mx = max(mx, summ)
                l += 1
                    
            elif summ == k:
                r -= 1
            else:
                r -= 1
        return mx
    
    # 1, 8, 23, 24, 33, 34, 54, 75
                
        