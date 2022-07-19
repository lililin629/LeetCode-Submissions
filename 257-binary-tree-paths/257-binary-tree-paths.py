# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path, paths = [root], []
        self.find_path(root, path, paths)
        return paths
        
    
    def find_path(self, node, path, paths):
        if not node:
            return
        if not node.left and not node.right:
            paths.append("->".join([str(n.val) for n in path]))
            return
        
        path.append(node.left)
        self.find_path(node.left, path, paths)
        path.pop()
        
        path.append(node.right)
        self.find_path(node.right, path, paths)
        path.pop()
        