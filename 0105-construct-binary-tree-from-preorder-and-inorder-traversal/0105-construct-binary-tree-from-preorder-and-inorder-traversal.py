# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return 
        root_val = preorder[0]
        root = TreeNode(root_val)
        idx = inorder.index(root_val)
        
        l_in = inorder[:idx]
        r_in = inorder[idx+1:]
        l_pre = preorder[1:1+len(l_in)]
        r_pre = preorder[1+len(l_in):]
        
        root.left = self.buildTree(l_pre,l_in)
        root.right = self.buildTree(r_pre,r_in)
        return root
        
        