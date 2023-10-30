class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = Counter(s)
        dt = Counter(t)
        if ds == dt:
            return True
        return False
        