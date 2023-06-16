# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        
        depth = 0
        while queue:
            cur_level = len(queue)
            depth += 1
            for i in range(cur_level):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)

                if cur.right:
                    queue.append(cur.right)
        return depth