class Solution:
    def numSquares(self, n: int) -> int:
        q = deque([n])
        lev = -1
        seen = set([n])
        while q:
            # print(q)
            size = len(q)
            lev += 1
            for _ in range(size):
                num = q.popleft()
                if num == 0:
                    return lev
                if num > 0:
                    fac = math.floor(num**(0.5))
                    for j in range(1, fac+1):
                        remain = num - j**2
                        if remain not in seen:
                            q.append(remain)
                            seen.add(remain)
        return -1
                
        