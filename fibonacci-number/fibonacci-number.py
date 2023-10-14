class Solution:
    def fib(self, n: int) -> int:
        # cache = defaultdict(int)
        # cache[0] = 0
        # cache[1] = 1
        # for i in range(2, n+1):
        #     cache[i] = cache[i-2] + cache[i-1]
        # return cache[n]
        
          
        cache = {}
        return self.recur_fib(n, cache)
        
    def recur_fib(self, N, cache):
        if N in cache:
            return cache[N]

        if N < 2:
            cache[N] = N
        else:
            cache[N] = self.recur_fib(N-1, cache) + self.recur_fib(N-2, cache)

        # put result in cache for later reference.
        return cache[N]
        

       
        
        
        