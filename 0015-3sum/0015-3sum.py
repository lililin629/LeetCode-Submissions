class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        ans = set()
        for i in range(len(nums)):
            num = nums[i]
            if num in seen:
                continue
            seen.add(num)
            ls = self.twoSum(i, nums, -num)
            for l in ls:
                a = list(l)
                a.append(num)
                a.sort()
                ans.add(tuple(a))
        ret = []
        for an in ans:
            b = list(an)
            ret.append(b)
        return ret
    
    def twoSum(self, i, nums, target):
        l = 0
        r = len(nums)-1
        s = set()
        while l < r:
            if l == i:
                l += 1
                continue
            if r == i:
                r -= 1
                continue
            if nums[l] + nums[r] == target:
                s.add((nums[l], nums[r]))
                r -= 1
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
        return s
            
            
        
        