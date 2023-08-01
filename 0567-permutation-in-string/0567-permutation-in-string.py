class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = defaultdict(int)
        for c in s1:
            dic1[c] += 1
        
        l = 0
        r = len(s1) - 1
        
        dic2 = defaultdict(int)
        for c in s2[l:r+1]:
            dic2[c] += 1
        if self.check(dic1, dic2):
            return True
        
        
        for _ in range(len(s2) - len(s1)):
            dic2[s2[l]] -= 1
            l += 1
            r += 1
            dic2[s2[r]] += 1
            if self.check(dic1, dic2):
                    return True
        return False
                
    def check(self, dic1, dic2):
        for ch, fre in dic1.items():
            if dic2[ch] != fre:
                return False
        return True
            
                
        