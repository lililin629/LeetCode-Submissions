# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        lev = 0
        
        while q:
            lev += 1
            for _ in range(len(q)):
                cur = q.popleft()
                if not cur.left and not cur.right:
                    return lev
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                
        ############################DFS################################
        # if not root:
        #     return 0
        # if not root.left:
        #     return 1 + self.minDepth(root.right)
        # if not root.right:
        #     return 1 + self.minDepth(root.left)
        # return 1 + min(self.minDepth(root.right), self.minDepth(root.left))
            
        