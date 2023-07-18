# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # root, left, right
        self.total = 0
        def helper(root, cur_num):
            if root:
                cur_num = cur_num*10 + root.val
                if not root.left and not root.right:
                    self.total += cur_num
                    return
                helper(root.left, cur_num)
                helper(root.right, cur_num)
                

        
        helper(root, 0)
        
        return self.total
            
            
            
            
        