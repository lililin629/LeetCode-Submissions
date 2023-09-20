class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lst = [0]*1001
        for [p, s, e] in trips:
            lst[s] += p
            lst[e] -= p
        
        prefix = 0
        for p in lst:
            prefix += p
            if prefix > capacity:
                return False
        return True
            
        
        
        