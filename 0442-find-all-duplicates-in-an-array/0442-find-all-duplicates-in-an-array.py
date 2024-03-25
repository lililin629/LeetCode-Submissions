class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        ans = []
        for num in d:
            if d[num] > 1:
                ans.append(num)
        return ans
                
        