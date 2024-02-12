class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        length = [1]*len(nums)
        pre = [-1]*len(nums)
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] % nums[i] == 0:
                    if length[j] < length[i] + 1:
                        pre[j] = i
                        length[j] = length[i] + 1
        mx = max(length)
        end = 0
        for i, l in enumerate(length):
            if l == mx:
                end = i
                break
        
        ans = []
        while end != -1:
            ans.append(nums[end])
            end = pre[end]
        return ans
            
        
            
                
        
                
                    
        
                
        
      
                
        
                
            
            
        
        
#         nums.sort()
#         ans = []
#         self.mx = 0
#         self.dfs(nums, 0, [], ans)
#         return ans
    
#     def dfs(self, nums, idx, cur, ans):
#         if len(cur) > self.mx:
#             self.mx = len(cur)
#             ans = list(cur)
        
#         for i in range(idx, len(nums)):
#             cur.append(nums[idx])
            
#             cur.pop()
        
        