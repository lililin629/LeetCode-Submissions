class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        d = {}
        if not root:
            return 0
        self.dfs(root, 0, d)
        return sum(d[max(d)])
        
    def dfs(self, node, depth, d):
        if not node:
            return 
        if depth not in d:
            d[depth] = [node.val]
        else:
            d[depth].append(node.val)
        
        if node.left:
            self.dfs(node.left, depth + 1, d)
        if node.right:
            self.dfs(node.right, depth + 1, d)
        