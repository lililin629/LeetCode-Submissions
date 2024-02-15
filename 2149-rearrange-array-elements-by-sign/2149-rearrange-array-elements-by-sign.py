class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        
        ans = []
        p = 0
        while p < len(neg):
            ans.append(pos[p])
            ans.append(neg[p])
            p += 1
        return ans
        