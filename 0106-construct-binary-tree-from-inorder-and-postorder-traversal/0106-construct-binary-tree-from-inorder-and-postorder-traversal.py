# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return
        head_val = postorder[-1]
        head = TreeNode(head_val)
        
        in_idx = inorder.index(head_val)
        
        left_in = inorder[:in_idx]
        right_in = inorder[in_idx+1:]
        
        left_pos = postorder[:len(left_in)]
        right_pos = postorder[len(left_in):-1]
        
        head.left = self.buildTree(left_in, left_pos)
        head.right = self.buildTree(right_in, right_pos)
        
        return head
        
        
        