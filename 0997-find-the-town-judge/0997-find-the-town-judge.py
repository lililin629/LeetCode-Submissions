class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
        trusted = defaultdict(int)
        trusting = defaultdict(int)
        pos = []
        for [t, j] in trust:
            trusted[j] += 1
            trusting[t] += 1
            if trusted[j] == n-1:
                pos.append(j)
        for c in pos:
            if trusting[c] == 0:
                return c
        return -1
        