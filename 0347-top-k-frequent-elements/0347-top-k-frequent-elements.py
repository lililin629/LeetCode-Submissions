class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        ls = []
        for key in dic:
            ls.append((dic[key], key))
        ls.sort(reverse=True)
        
        ans = []
        for i in range(k):
            ans.append(ls[i][1])
        return ans
            
            
            
            
        