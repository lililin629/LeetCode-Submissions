# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        ls1 = []
        ls2 = []
        
        def dfs1(root):
            if not root:
                return 
            else:
                dfs1(root.left)
                dfs1(root.right)
                if not root.left and not root.right:
                    ls1.append(root.val)
                
        def dfs2(root):
            if not root:
                return 
            else:
                dfs2(root.left)
                dfs2(root.right)
                if not root.left and not root.right:
                    ls2.append(root.val)
            
            
        dfs1(root1)
        dfs2(root2)
        
        if ls1 == ls2:
            return True
        return False
                