# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        print(self.isSmaller(root.left, root.val))
        print(self.isBigger(root.right, root.val))
        
        return self.isSmaller(root.left, root.val) and self.isBigger(root.right, root.val) and self.isValidBST(root.left) and self.isValidBST(root.right)
    
    def isSmaller(self, rootS, B):
        if not rootS:
            return True
        if rootS.val >= B:
            return False
        return self.isSmaller(rootS.left, B) and self.isSmaller(rootS.right, B)
        
    def isBigger(self, rootB, S):
        if not rootB:
            return True
        if rootB.val <= S:
            return False
        return self.isBigger(rootB.left, S) and self.isBigger(rootB.right, S)
        
        
        