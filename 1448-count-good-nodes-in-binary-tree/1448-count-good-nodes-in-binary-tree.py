# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, maxv):
            
            if not root:
                return 0
            is_max = 0
            if root.val >= maxv:
                is_max = 1
                maxv = root.val
            gl = dfs(root.left, maxv)
            gr = dfs(root.right, maxv)
            return gl + gr + is_max
                
        
        
        #initialize
        maxv = float('-inf')
        return dfs(root, maxv)
        