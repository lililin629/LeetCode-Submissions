# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = []
        odd = True
        
        while q:
            lev = len(q)
            res = []
            for i in range(lev):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                res.append(node.val)
            if odd:
                ans.append(res)
                odd = False
            else:
                ans.append(res[::-1])
                odd = True
        return ans
            
                
            
        