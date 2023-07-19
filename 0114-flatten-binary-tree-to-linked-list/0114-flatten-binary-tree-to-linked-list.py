# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # root left rihgt
        if not root:
            return
        left = self.flatten(root.left)
        right = self.flatten(root.right)
        
        if left:
            cur = left
            while cur.right:
                cur = cur.right
            cur.right = right
            root.right = left
        
        root.left = None
        return root
        
            