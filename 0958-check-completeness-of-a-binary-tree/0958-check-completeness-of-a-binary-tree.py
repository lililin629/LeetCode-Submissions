# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        had_null = False
        
        while q:
            cur = q.popleft()
            
            if not cur.left:
                had_null = True
            if cur.left:
                if had_null:
                    return False
                q.append(cur.left)
            if not cur.right:
                had_null = True
            if cur.right:
                if had_null:
                    return False
                q.append(cur.right)
            
        return True
        
        
        
#         if self.diff_h(root.left, root.right) == -1:
#             return False
#         if self.diff_h(root.left, root.right) == 1:
            
#     def diff_h(self, r1, r2):
#         if abs(self.h(r1, 0) - self.h(r2, 0)) == 1:
#             return 1
#         if abs(self.h(r1, 0) - self.h(r2, 0)) == 0:
#             return 0
#         return -1
    
#     def h(self, root, h):
#         if not root:
#             return h
#         return max(self.h(root.left, h + 1), self.h(root.right, h + 1))
    
#     def complete(self, root):
#         if not root:
#             return True
#         if not root.left and not root.right:
#             return True
#         if not root.left and root.right:
#             return False
#         if not self.full(root.left) and root.right:
#             return False
#         return self.complete(root.left) and self.complete(root.right)
    
#     def full(self, root):
#         if not root:
#             return True
#         if not root.left and not root.right:
#             return True
#         if not root.left or not root.right:
#             return False
#         return True
        
        