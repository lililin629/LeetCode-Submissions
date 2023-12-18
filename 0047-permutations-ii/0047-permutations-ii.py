class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []
        self.perm(ans, nums, set(), [])
        return ans
    
    def perm(self, ans, nums, visited, cur):
        if len(cur) == len(nums):
            ans.append(cur)
            return
        
        for i in range(len(nums)):
            if i in visited:
                continue
            if i > 0 and nums[i] == nums[i-1] and (i-1) not in visited:
                continue
                
            
            visited.add(i)
            self.perm(ans, nums, visited, cur+[nums[i]])
            visited.remove(i)
            
        
        