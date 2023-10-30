class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        
        dt = Counter(t)
        ds = defaultdict(int)
        
        min_l = float('inf')
        ans = ''
        l = 0
        for r in range(len(s)):
            if s[r] in dt:
                ds[s[r]] += 1
                
            while l <= r and self.isValid(dt, ds):
                if r-l+1 < min_l:
                    min_l = r-l+1
                    ans = s[l:r+1]
                if s[l] in dt:
                    ds[s[l]] -= 1
                    # if ds[s[l]] == 0:
                    #     del ds[s[l]]
                l += 1
       
        return ans
    
    def isValid(self, d1, d2):
        for key in d1:
            if d2[key] < d1[key]:
                return False
        return True
            
                
        
            
            
        