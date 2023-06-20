class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ls = []
        t_ls = []
        for ch in s:
            s_ls.append(ch)
        for ch in t:
            t_ls.append(ch)
        s_ls.sort()
        t_ls.sort()
        if s_ls == t_ls:
            return True
        return False
            
        