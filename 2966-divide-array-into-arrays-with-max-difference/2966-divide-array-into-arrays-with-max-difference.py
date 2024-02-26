class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = [[0, 0, 0] for _ in range(len(nums)//3)]
        for i, num in enumerate(nums):
            x = i//3
            y = i%3
            ans[x][y] = num
            if y == 2:
                if num-ans[x][0] > k:
                    return []
        return ans
            
        
            
            
        