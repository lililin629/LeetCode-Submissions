class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
    
        q = deque([0])
        step = 0
        visited = set([0])
        
        while q:
            level = len(q)
            step += 1
            for _ in range(level):
                cur = q.popleft()
                for i in range(nums[cur]):
                    if i+1+cur == len(nums)-1:
                        return step
                    if i+1+cur not in visited:
                        q.append(i+1+cur)
                        visited.add(i+1+cur)
        
                
        