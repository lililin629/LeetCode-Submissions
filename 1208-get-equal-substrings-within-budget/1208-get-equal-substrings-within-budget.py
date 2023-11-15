class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        dist = defaultdict(int)
        
        for i in range(n):
            dist[i] = abs(ord(s[i]) - ord(t[i]))
        
        l = r = 0
        dif = 0
        mx = 0
        
        while r < n:
            dif += dist[r]
            if dif <= maxCost:
                mx = max(mx, r-l+1)
            else:
                dif -= dist[l]
                l += 1
            r += 1
        return mx
                
            
            
        
       
                
                
        