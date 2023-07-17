# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        height-balanced: 
        for every node in the tree, the height of the left and right subtrees 
        differ by at most one.
        '''
        if not root:
            return True
        left = self.height(root.left, 0)
        right = self.height(root.right, 0)
        if abs(left - right) > 1:
            return False
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
    
    def height(self, root, h):
        if not root:
            return h
        l = self.height(root.left, h + 1)
        r = self.height(root.right, h + 1)
        return max(l, r)
        
        
        
        