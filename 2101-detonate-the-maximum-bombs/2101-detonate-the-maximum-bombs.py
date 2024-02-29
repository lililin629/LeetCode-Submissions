class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        count = 0
        for i, b in enumerate(bombs):
            count = max(self.bfs(i, bombs), count)
        return count
    
    def bfs(self, i, bombs):
        q = deque()
        [x, y, r] = bombs[i]
        q.append((x, y, r))
        used = set()
        used.add((i, x, y))
        count = 1
        
        while q:
            cx, cy, cr = q.popleft()
            
            for j, [a, b, c] in enumerate(bombs):
                if (j, a, b) not in used and self.dist(a,b,cx,cy) <= cr:
                    q.append((a, b, c))
                    used.add((j, a, b))
                    count += 1
        return count
    
    def dist(self, a, b, c, d):
        return ((a-c)**2 + (b-d)**2)**(1/2)
        
                    
                    
            
            
        