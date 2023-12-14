class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # right i, j++
        # down i++, j
        # left i, j--
        # up i--, j
        def turn_right(d):
            if d == 'r':
                return 'd'
            elif d == 'l':
                return 'u'
            elif d == 'd':
                return 'l'
            elif d == 'u':
                return 'r'
        def forward(d, x, y):
            if d == 'r':
                return (x, y + 1)
            if d == 'l':
                return (x, y-1)
            if d == 'd':
                return (x + 1, y)
            if d == 'u':
                return (x-1, y)
        def wall(x, y):
            if 0 <= x < m and 0 <= y < n:
                return False
            return True
            
            
        if not matrix:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        visited = set()
        ans = []
        i = j = 0
        direction = 'r'
        
        visited.add((i, j))
        ans.append(matrix[i][j])
        ni, nj = forward(direction, i, j)
       
        
        while len(visited) < m*n:
            
            if (ni, nj) in visited or wall(ni, nj):
                direction = turn_right(direction)
                ni, nj = forward(direction, i, j)
            else:
                i, j = ni, nj
                visited.add((i, j))
                ans.append(matrix[i][j])
                ni, nj = forward(direction, i, j)
        return ans
        
        