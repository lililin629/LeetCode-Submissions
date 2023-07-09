# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return root.val
        else:
            left, d1 = self.dfs(root.left)
            right, d2 = self.dfs(root.right)
            if d1 == d2:
                return left + right
            else:
                if d1 > d2:
                    return left
                return right
        
    def dfs(self, root):
        if not root:
            return 0, 0
        if not root.left and not root.right:
            return root.val, 1
        else:
            left, d1 = self.dfs(root.left)
            right, d2 = self.dfs(root.right)
            if d1 == d2:
                return left + right, d1+1
            else:
                if d1 > d2:
                    return left, d1+1
                return right, d2+1
            
            
            
        
        
                
            
            
        