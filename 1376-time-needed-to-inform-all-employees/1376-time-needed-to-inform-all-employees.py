class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """
        2
        0 3
        1 4
        """
        if n == 1:
            return 0
        graph = defaultdict(list)
        for sub, mng in enumerate(manager):
            if mng != -1:
                graph[mng].append(sub)
        
        # {2:[0, 3], 0:[1], 3:[4]}
        q = deque([(headID, 0)])
        max_time = 0
        while q:
            cur, cur_time = q.popleft()
            max_time = max(max_time, cur_time)
           
            for nx in graph[cur]:
                q.append((nx, cur_time+informTime[cur]))
        return max_time
        
        
        
        
   