class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*n
        dp[n-1] = True
        
        for i in range(n-2, -1, -1):
            steps = nums[i]
            farthest = min(i+steps+1, n)
            for j in range(i+1, farthest):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]
#         if len(nums) == 1:
#             return True
#         q = deque([0])
#         visited = {0}
        
#         while q:
#             cur = q.popleft()
#             for i in range(nums[cur]):
#                 if i+1+cur >= len(nums)-1:
#                     return True
                    
#                 if i+1+cur not in visited:
#                     q.append(i+1+cur)
#                     visited.add(i+1+cur)
#         return False
                    
        