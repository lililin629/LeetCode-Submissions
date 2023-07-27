# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        ans = []
        
        while q:
            cur = []
            length = len(q)
            for i in range(length):
                node = q.popleft()
                cur.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(cur)
        
        ans2 = []
        for i in range(len(ans)-1, -1, -1):
            ans2.append(ans[i])
        return ans2
            
            
                
                
        