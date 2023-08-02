class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                m.append(matrix[i][j])
        l = 0
        r = len(m)-1
        
        while l + 1 < r:
            mid = (l + r)//2
            if m[mid] == target:
                return True
            elif m[mid] > target:
                r = mid
            else:
                l = mid
        
        if m[l] == target or m[r] == target:
            return True
        return False
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         m = []
        
#         for ls in matrix:
#             for c in ls:
#                 m.append(c)
        
#         if len(m) < 1:
#             return False
        
#         s = 0
#         e = len(m) - 1
#         while s + 1 < e:
#             mid = (s + e) // 2 
#             if m[mid] == target:
#                 return True
#             if m[mid] < target:
#                 s = mid
#             if m[mid] > target:
#                 e = mid
#         if m[s] == target:
#             return True
#         if m[e] == target:
#             return True
#         return False
        