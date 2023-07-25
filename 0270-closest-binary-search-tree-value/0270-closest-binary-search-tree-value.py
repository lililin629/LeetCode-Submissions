# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.minv = float('inf')
        self.ans = 0
        
        def dfs(root):
            if not root:
                return 
            
            if abs(root.val - target) < self.minv:
                self.minv = abs(root.val - target)
                self.ans = root.val
            if abs(root.val - target) == self.minv:
                self.ans = min(self.ans, root.val)
                
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return self.ans
    
            
                    
            
            
            
            
        