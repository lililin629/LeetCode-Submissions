# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(root, s):
            if not root.left and not root.right:
                ans.append(s) 
                return
            if root.left:
                dfs(root.left, s+'->'+str(root.left.val))
            if root.right:
                dfs(root.right, s+'->'+str(root.right.val))
        dfs(root, str(root.val))
        return ans
            


