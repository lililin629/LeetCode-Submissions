# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
        
        
#         def trim(root):
#             if not root:
#                 return None

#             if root.val < low:
#                 return trim(root.right)
#             if root.val > high:
#                 return trim(root.left)
#             if root.val >= low and root.val <= high:
#                 root.left = trim(root.left)
#                 root.right = trim(root.right)
#                 return root

#         return trim(root)
            
                
                
        