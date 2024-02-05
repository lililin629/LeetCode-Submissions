# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = defaultdict(list)
        nodes = []
        q = deque()
        q.append((root, 0))
        
        while q:
            node, x_pos = q.popleft()
            ans[x_pos].append(node.val)
            
            if node.left:
                q.append((node.left, x_pos-1))
                
            if node.right:
                q.append((node.right, x_pos+1))
        
        ans = dict(sorted(ans.items()))
        res = []
        for k in ans:
            res.append(ans[k])
        return res
            
        
        
            
            
        