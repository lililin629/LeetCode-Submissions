# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
    
        suc = None 
        # left root right
        while root:
            if root.val > p.val:
                suc = root
                root = root.left
            else:
                root = root.right
        return suc


       
        
                
        
        