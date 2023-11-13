# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         memo = defaultdict(bool) # {(x, y, length): True}
#         m = len(matrix)
#         n = len(matrix[0])
#         mx = max(m, n)
#         mx_len = 0
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == '1':
#                     mx_len = 1
#                     memo[(1, i, j)] = True
        
#         for length in range(2, mx+1):
#             for i in range(m):
#                 for j in range(n):
#                     if memo[(length-1, i, j)] and self.check_l(i, j, length, m, n, matrix):
                    
#                         memo[(length, i, j)] = True
#                         mx_len = max(mx_len, length)
#         # print(memo)
#         return mx_len**2

#     def check_l(self, i, j, l, m, n, matrix):
#         s = set()
#         for x in range(l):
#             if 0 <= i+x < m and  0 <= j+l-1 < n and matrix[i+x][j+l-1] == '1':
#                 s.add((i+x, j+l-1))
#             if 0 <= i+l-1 < m and  0 <= j+x < n and matrix[i+l-1][j+x] == '1':
#                 s.add((i+l-1, j+x))
#         if len(s) == 2*l -1:
#             return True
#         return False
                        
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        max_side = 0

        # Optionally, use a separate dp table if modifying matrix is not allowed
        # dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                     matrix[i][j] = 1
                else:
                    matrix[i][j] = 0
                    
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1

                    max_side = max(max_side, matrix[i][j])

        return max_side ** 2
            
        