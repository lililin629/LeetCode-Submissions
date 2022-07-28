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
        self.helper(root)
        
    def helper(self, root):
        if not root:
            return None
        # flatten left
        left_end = self.helper(root.left)
        # flatten right
        right_end = self.helper(root.right)
        # connect
        if left_end is not None:
            left_end.right = root.right
            root.right = root.left
            root.left = None
        return right_end or left_end or root
        
        
        
        