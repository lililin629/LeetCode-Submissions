# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            if root.val == targetSum:
                return True
        new_t = targetSum - root.val
        return self.hasPathSum(root.left, new_t) or self.hasPathSum(root.right, new_t)
        