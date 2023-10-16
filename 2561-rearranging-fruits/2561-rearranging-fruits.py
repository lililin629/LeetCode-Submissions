class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        d1 = Counter(basket1)
        d2 = Counter(basket2)
        d = Counter(basket1+basket2)
        
        change = []
        for key, val in d.items():
            if val%2 == 1:
                return -1
            val //= 2
            
            if val < d1[key]:
                change.append((key, abs(val-d1[key])))
            if val < d2[key]:
                change.append((key, abs(val-d2[key])))
        ans = []
        for (key, val) in change:
            for _ in range(val):
                ans.append(key)
        
        ans.sort()
        cost = 0
        
        smallest = min(basket1+basket2)
        
        for a in ans[:len(ans)//2]:
            if a < smallest*2:
                cost += a
            else:
                cost += smallest*2
        
        return cost
        
        
        
        
        
        
        
            
            
        