class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph, stops = defaultdict(list), [float('inf')]*n
        for f, to, price in flights:
            graph[f].append([to, price])
            
        q = [(0, src, 0)]
        while q:
            pr, node, steps = heapq.heappop(q)
            if steps > stops[node] or steps > k + 1:
                continue
            stops[node] = steps
            if node == dst:
                return pr
            if node in graph and steps <= k:
                for neighbor, price in graph[node]:
                    if steps + 1 < stops[neighbor]:
                        heapq.heappush(q, (pr+price, neighbor, steps+1))
        return -1
        