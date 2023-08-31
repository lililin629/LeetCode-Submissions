# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root, targetSum, 0)
    
    def dfs(self, root, targetSum, cur_sum) -> bool:
        if not root:
            return
        
        cur_sum += root.val
        
        if not root.left and not root.right:
            if cur_sum == targetSum:
                return True
        
        if self.dfs(root.left, targetSum, cur_sum):
            return True
        if self.dfs(root.right, targetSum, cur_sum):
            return True
        
        
        
        
        