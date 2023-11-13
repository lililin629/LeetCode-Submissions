# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        
        first = None
        first_val = 0
        
        while q:
            lenq = len(q)
            first = q.popleft()
            first_val = first.val
            if first.left:
                q.append(first.left)
            if first.right:
                q.append(first.right)
                
            for _ in range(lenq-1):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return first_val
                
                
                
                
        
        