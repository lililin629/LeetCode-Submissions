class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        queue = deque([(sr, sc)])
        visited = {(sr, sc)}
        
        while queue:
            cur_x, cur_y = queue.popleft()
            image[cur_x][cur_y] = color
            for dx, dy in dirs:
                new_pos = cur_x+dx, cur_y+dy
                if self.valid(new_pos, image):
                    if new_pos not in visited:
                        if image[new_pos[0]][new_pos[1]] == orig:
                            queue.append(new_pos)
                            visited.add(new_pos)
        return image
    
    def valid(self, new_pos, image):
        m = len(image)
        n = len(image[0])
        if new_pos[0] < 0 or new_pos[0] >= m or new_pos[1] < 0 or new_pos[1] >= n:
            return False
        return True
        
                    
                
        
        
        
        