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
        nodes = deque([root])
        ans = [[root.val]]
        
        while nodes:
            l = len(nodes)
            res = []
            for _ in range(l):
                node = nodes.popleft()
                if node.left:
                    nodes.append(node.left)
                    res.append(node.left.val)
                if node.right:
                    nodes.append(node.right)
                    res.append(node.right.val)
            if res:
                ans.append(res) 
        return ans