# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        ans = []
        
        while q:
            n = len(q)
            lev = []
            for i in range(n):
                r = q.popleft()
                lev.append(r.val)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            
            ans.append(lev)
        return ans
        