class Solution:
    def romanToInt(self, s: str) -> int:
        # IVX XLC  CDM
        d = defaultdict(set)
        for i, c in enumerate(s):
            d[c].add(i)
        
        ans = 0
        for idx in d['I']:
            if idx + 1 in d['V'] or idx + 1 in d['X']:
                ans -= 1
            else:
                ans += 1
        for idx in d['V']:
            ans += 5
        
        for idx in d['X']:
            if idx + 1 in d['L'] or idx + 1 in d['C']:
                ans -= 10
            else:
                ans += 10
        
        for idx in d['L']:
            ans += 50
        
        for idx in d['C']:
            if idx + 1 in d['D'] or idx + 1 in d['M']:
                ans -= 100
            else:
                ans += 100
        
        for idx in d['D']:
            ans += 500
        
        for idx in d['M']:
            ans += 1000
        
        return ans
        
        
        
        
        
        
        
        
                
            
        
        