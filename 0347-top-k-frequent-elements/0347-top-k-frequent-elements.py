class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        d2 = defaultdict(list)
        
        s = set()
        for num, fre in d.items():
            s.add(fre)
            d2[fre].append(num)
        
        lst = list(s)
        lst.sort(reverse = True)
        
        
        ans = []
        for i in range(len(lst)):
            key = lst[i]
            for num in d2[key]:
                ans.append(num)
                k -= 1
            if k == 0:
                break
        return ans
            
        
        
        
        
        
            
        