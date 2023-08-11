class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        s = set()
        count = 0
        
        for num in nums:
            s.add(num)
            d[num] += 1
        
        if k != 0:
            for n in s:
                if n+k in s:
                    count += 1
        if k == 0:
            for n in s:
                if d[n] > 1:
                    count += 1
        return count
        

#         nums = sorted(nums)

#         left = 0
#         right = 1

#         result = 0

#         while (left < len(nums) and right < len(nums)):
#             if (left == right or nums[right] - nums[left] < k):
#                 # List item 1 in the text
#                 right += 1
#             elif nums[right] - nums[left] > k:
#                 # List item 2 in the text
#                 left += 1
#             else:
#                 # List item 3 in the text
#                 left += 1
#                 result += 1
#                 while (left < len(nums) and nums[left] == nums[left - 1]):
#                     left += 1

#         return result