class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.helper(nums, permutations, [], set())
        return permutations
    
    
    def helper(self, nums, permutations, cur, visited):
        if len(cur) == len(nums):
            permutations.append(list(cur))
            
        for num in nums:
            if num in visited:
                continue
            cur.append(num)
            visited.add(num)
            self.helper(nums, permutations, cur, visited)
            cur.pop()
            visited.remove(num)
            
        
        