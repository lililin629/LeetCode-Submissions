# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_bal, height = self.helper(root)
        return is_bal
    
    
    def helper(self, root):
        if not root:
            return True, 0
        is_bal_left, height_left = self.helper(root.left)
        is_bal_right, height_right = self.helper(root.right)
        
        if is_bal_left and is_bal_right and abs(height_left-height_right) < 2:
            return True, max(height_right, height_left) + 1
        return False, max(height_right, height_left) + 1
        
        
    
    
        