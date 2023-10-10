# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf'), float('inf'))
    
    def helper(self, root, low, hi):
        if not root:
            return True
        # if not root.left and not root.right:
        #     return True
        if root.val <= low or root.val >= hi:
            return False
        
        return self.helper(root.left, low, root.val) and self.helper(root.right, root.val, hi)
        