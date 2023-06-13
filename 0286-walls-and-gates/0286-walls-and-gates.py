class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    door = (i, j)
                    self.bfs(door, rooms)

    def bfs(self, door, rooms):
        queue = deque([door])
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        count = 0

        while queue:
            curr_level_cnt = len(queue)
            count += 1
            for i in range(curr_level_cnt):
                cur_x, cur_y = queue.popleft()
                for offset_x, offset_y in directions:
                    next_x, next_y = cur_x + offset_x, cur_y + offset_y
                    if self.valid((next_x, next_y), rooms):
                        if (next_x, next_y) not in visited:
                            rooms[next_x][next_y] = min(count, rooms[next_x][next_y])
                            queue.append((next_x, next_y))
                            visited.add((next_x, next_y))
           
    
    
    def valid(self, next, rooms):
        # if next_x, next_y is within limit
        m = len(rooms)-1
        n = len(rooms[0])-1
        if next[0] < 0 or next[0]> m:
            return False
        if next[1] < 0 or next[1]> n:
            return False
        # if next_x, next_y is space
        if rooms[next[0]][next[1]] == -1 or rooms[next[0]][next[1]] == 0:
            return False
        
        return True