class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        q = deque([0])
        visited = {0}
        
        while q:
            cur = q.popleft()
            for i in range(nums[cur]):
                if i+1+cur >= len(nums)-1:
                    return True
                    
                if i+1+cur not in visited:
                    q.append(i+1+cur)
                    visited.add(i+1+cur)
        return False
                    
        