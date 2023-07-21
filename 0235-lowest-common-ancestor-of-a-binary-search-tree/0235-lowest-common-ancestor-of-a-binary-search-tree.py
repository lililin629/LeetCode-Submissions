# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        big = p.val if p.val > q.val else q.val
        small = p.val if p.val < q.val else q.val
        print(big)
        print(small)
        
        if not root:
            return
        if root.val == big or root.val == small:
            return root
        if root.val < big and root.val > small:
            return root
        if root.val < small:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > big:
            return self.lowestCommonAncestor(root.left, p, q)
            
        