class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        left = 0
        
        bad = 0
        for i in range(n):
            if nums[i] > nums[i+1]:
                bad += 1
        if bad > 1:
            return False
        if bad == 0:
            return True
                
        for i in range(n):
            if nums[i] <= nums[i+1]:
                left += 1
            else:
                break
        
        right = left + 1
        
        if left == 0 or right == n:
            return True
        prev = left - 1
        nex = right + 1
        
        if nums[right] >= nums[prev]:
            return True
        if nums[nex] >= nums[left]:
            return True
        return False
            
            