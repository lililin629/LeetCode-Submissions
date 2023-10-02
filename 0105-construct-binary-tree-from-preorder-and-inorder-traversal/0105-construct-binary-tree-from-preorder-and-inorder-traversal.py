# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if len(preorder) == 0:
            return None
        root = preorder[0]
        if len(preorder) == 1:
            return TreeNode(root)


        in_idx = inorder.index(root)

        in_left = inorder[:in_idx]
        in_right = inorder[in_idx+1:]
        pre_left = preorder[1:1+in_idx]
        pre_right = preorder[1+in_idx:]

        l = self.buildTree(pre_left, in_left)
        r = self.buildTree(pre_right, in_right)

        return TreeNode(root, l, r)
   
        