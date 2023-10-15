# #class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         r = len(matrix)-1
#         c = len(matrix[0])-1
#         return self.helper(matrix, target, 0, r, 0, c)
        
        
    
#     def helper(self, matrix, target, start_r, end_r, start_c, end_c):
#         if start_r > end_r or start_c > end_c:
#             return False
#         midr = (start_r + end_r)//2
#         lo, hi = self.binary(matrix[midr], target)
#         print(f"{matrix[midr][lo]}, {matrix[midr][hi]}")
#         if matrix[midr][lo] == target:
#             return True
#         if matrix[midr][hi] == target:
#             return True
            
#         # matrix[midr][l] < target < matrix[midr][r]
#         # 右上 or 左下
#         # If not found, search in the top right or bottom left
#         top_right = self.helper(matrix, target, start_r, midr-1, hi, end_c) if matrix[midr][hi] < target else False
#         bottom_left = self.helper(matrix, target, midr+1, end_r, start_c, lo) if matrix[midr][lo] > target else False
        
#         return top_right or bottom_left
    
#     def binary(self, ls, target):
#         l = 0
#         r = len(ls)-1
#         while l + 1 < r:
#             mid = (l+r)//2
#             if ls[mid] == target:
#                 return (mid, mid)
#             if ls[mid] < target:
#                 l = mid
#             if ls[mid] > target:
#                 r = mid
#         return (l, r)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        row, col = 0, len(matrix[0]) - 1
        
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
                
        return False

