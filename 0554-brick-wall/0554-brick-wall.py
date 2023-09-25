class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        d = defaultdict(int)
        
        for lst in wall:
            ps = 0
            for i in lst[:-1]:
                ps += i
                d[ps] += 1
        # {1: 3, 3: 3,... }
        if not d:
            return len(wall)
        
        n = len(wall)
        
        ans = float('inf')
        for k in d:
            hit = n - d[k]
            ans = min(ans, hit)
        
        return ans
            
                    
            
                
        