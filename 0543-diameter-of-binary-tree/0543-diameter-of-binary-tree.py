# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = self.diameterOfBinaryTree(root.left)
        r = self.diameterOfBinaryTree(root.right)
        m = self.lp(root.left, 0) + self.lp(root.right, 0) + 2
        return max(l, r, m)
    
    def lp(self, r, h):
        if not r:
            return -1
        if not r.left and not r.right:
            return h
        l = self.lp(r.left, h+1)
        r = self.lp(r.right, h+1)
        
        return max(l, r)
        
        
        
        
        