class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 or k == 1:
            return 0
        a = (k-1) // 2
        b = (k-1) % 2
        ancestor = self.kthGrammar(n-1, a+1)
        if ancestor == 0:
            return 1 if b else 0
        if ancestor == 1:
            return 0 if b else 1
        