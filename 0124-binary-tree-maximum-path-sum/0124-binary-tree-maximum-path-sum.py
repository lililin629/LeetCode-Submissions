# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
    
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
#         l = r = float('-inf')
#         if not root:
#             return 0
#         if not root.left and not root.right:
#             return root.val
#         if root.left:
#             l = self.maxPathSum(root.left)
#         if root.right:
#             r = self.maxPathSum(root.right)
#         ld = self.direct(root.left) 
#         rd = self.direct(root.right)
#         rv = root.val
        
#         return max(l, r, rv, rv + max(rd, ld, rd+ld))
    
#     def direct(self, node):
        
#         if not node:
#             return 0
#         l = self.direct(node.left)
#         r = self.direct(node.right)
       
#         return max(node.val, node.val + max(l, r))
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def direct(node):
            if not node:
                return 0
            if node in memo:
                return memo[node]

            # Calculate the maximum path sum starting from the current node
            left_max = direct(node.left)
            right_max = direct(node.right)
            memo[node] = max(node.val, node.val + max(left_max, right_max))
            return memo[node]

        def maxPath(node):
            if not node:
                return float('-inf')

            # Compute the maximum path sum through the current node
            left_max = direct(node.left)
            right_max = direct(node.right)
            current_max = node.val + max(0, left_max) + max(0, right_max)

            # Compare with the maximum path sums in the left and right subtrees
            return max(current_max, maxPath(node.left), maxPath(node.right))

        return maxPath(root)

