class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph, stops = defaultdict(list), [float('inf')]*n
        for f, to, price in flights:
            graph[f].append([to, price])
            
        q = [(0, src, 0)]
        while q:
            dist, node, steps = heapq.heappop(q)
            if steps > stops[node] or steps > k + 1:
                continue
            stops[node] = steps
            if node == dst:
                return dist
            if node not in graph:
                continue
            for neighbor, price in graph[node]:
                heapq.heappush(q, (dist+price, neighbor, steps+1))
        return -1
        