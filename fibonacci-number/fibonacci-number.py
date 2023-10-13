class Solution:
    def fib(self, n: int) -> int:
        cache = defaultdict(int)
        cache[0] = 0
        cache[1] = 1
        for i in range(2, n+1):
            cache[i] = cache[i-2] + cache[i-1]
        return cache[n]
        
        
        