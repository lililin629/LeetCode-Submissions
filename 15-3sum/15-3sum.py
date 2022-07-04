class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            self.two_sum(nums, i+1, len(nums)-1, -nums[i], ans)
        return ans
    
    def two_sum(self, lst, left, right,target, ans):
        last_pair = None
        while left < right:
            if lst[left] + lst[right] > target:
                right -= 1
            elif lst[left] + lst[right] < target:
                left += 1
            else:
                if (lst[left], lst[right]) != last_pair:
                    ans.append([-target, lst[left], lst[right]])
                last_pair = (lst[left], lst[right])
                left += 1
                right -= 1
                    
        return ans
                
        
        