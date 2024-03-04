# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans = 0
        self.dfs(root)
        return self.ans
        
    def dfs(self, root):
        if not root:
            return (0, 0)
        
        lsum, lcount = self.dfs(root.left)
        rsum, rcount = self.dfs(root.right)
        if (lsum+rsum+root.val)//(lcount+rcount+1) == root.val:
            self.ans += 1
        
        return (lsum+rsum+root.val, lcount+rcount+1)
            
            
        
        
        
        
        
        
        