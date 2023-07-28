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
            if root.val >= maxv:
                good[0] += 1
                maxv = root.val
            dfs(root.left, maxv)
            dfs(root.right, maxv)
                
        
        
        #initialize
        good = [0]
        maxv = float('-inf')
        dfs(root, maxv)
        return good[0]