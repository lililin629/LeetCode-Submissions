class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph, prices = defaultdict(list), [-1 for _ in range(n)]
        for f, to, price in flights:
            graph[f].append([to, price])
        prices[src], q, step = 0, deque([src]), 0
        while q and step <= k:
            sz = len(q)
            new_prices = list(prices)
            for _ in range(sz):
                cur = q.popleft()
                for neighbor, price in graph[cur]:
                    if new_prices[neighbor] == -1 or new_prices[neighbor] > prices[cur]+price:
                        new_prices[neighbor] = prices[cur] + price
                        q.append(neighbor)
            step += 1
            prices = new_prices
        return prices[dst]
        