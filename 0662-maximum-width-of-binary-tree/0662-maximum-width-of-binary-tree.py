# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         if not root.left and not root.right:
#             return 1
        
#         left = self.count_left(root.left, 1)

#         right = self.count_right(root.right, 1)
        
#         return left + right
    
#     def count_left(self, root, c1):
#         if not root:
#             return 0
#         while root:
#             if root.left:
#                 c1 *= 2
#                 root = root.left
#                 continue
#             if root.right:
#                 c1 = c1*2 - 1
#                 root = root.right
#         return c1
    
#     def count_right(self, root, c1):
#         if not root:
#             return 0
#         while root:
#             if root.right:
#                 c1 *= 2
#                 root = root.right
#                 continue
#             if root.left:
#                 c1 = c1*2 - 1
#                 root = root.left
#         return c1
    
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 0)])  # store nodes along with their positions
        max_width = 0
        while queue:
            level_length = len(queue)
            _, first = queue[0]
            for i in range(level_length):
                node, col_index = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*col_index))
                if node.right:
                    queue.append((node.right, 2*col_index + 1))
            max_width = max(max_width, col_index - first + 1)
        return max_width
