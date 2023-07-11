# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if subRoot and not root:
            return False
        if subRoot and root:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) or self.same(root, subRoot)
    
    def same(self, r1, r2):
        if not r1 and not r2:
            return True
        if r1 and not r2:
            return False
        if not r1 and r2:
            return False
        if r1 and r2:
            return r1.val == r2.val and self.same(r1.left, r2.left) and self.same(r1.right, r2.right)
    
    