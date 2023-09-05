class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for [x, y, cost] in connections:
            graph[x].append((cost, y))
            graph[y].append((cost, x))
        
        heap = [(0, 1)]
        heapq.heapify(heap)
        connected = set()
        total_cost = 0
        
        while heap:
            
            cur_cost, cury = heapq.heappop(heap)
            if cury not in connected:
                total_cost += cur_cost
                connected.add(cury)
                for (cost, ny) in graph[cury]:
                    if ny not in connected:
                        heapq.heappush(heap,(cost, ny))
            
        return total_cost if len(connected) == n else -1
            
            
            
        