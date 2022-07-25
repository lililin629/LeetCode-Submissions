DIRECTIONS = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        # build a dict to record distance to node
        node_dist_dict = {(0,0): 0}
        # BFS
        q = collections.deque([(0, 0)])
        # while queue: if (next_x, next_y) == (x, y) return dict[(next_x, next_y)]
        while q:
            x1, y1 = q.popleft()
            for dx, dy in DIRECTIONS:
                x2, y2 = x1+dx, y1+dy
                if x2 == x and y2 == y:
                    return node_dist_dict[(x1, y1)] + 1
                if (x2, y2) in node_dist_dict:
                    continue
                node_dist_dict[(x2, y2)] = node_dist_dict[(x1, y1)] + 1
                q.append((x2, y2))
                
       