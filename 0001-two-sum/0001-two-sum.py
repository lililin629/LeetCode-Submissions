class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = []
        for i in range(len(nums)):
            n.append((nums[i], i))
            
        n.sort()
        p1 = 0
        p2 = len(nums)-1
        
        
        while p1 < p2:
            if (n[p1][0] + n[p2][0]) == target:
                return [n[p1][1], n[p2][1]]
                
            else: 
                if (n[p1][0] + n[p2][0]) < target:
                    p1 += 1
                else:
                    p2 -= 1
        
        
           
                
        
        
        