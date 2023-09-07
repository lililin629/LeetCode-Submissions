# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root))
        
    
    
    def dfs(self, root):
        if not root:
            return (0, 0)
        # if rob root
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        v1 = root.val + left[1] + right[1]
        
        # not rob root
        v2 = max(left) + max(right)
        
        return v1, v2
        
        
        