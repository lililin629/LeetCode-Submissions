# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        ans = []
        
        self.helper(root, ans)
        
        for i in range(len(ans)):
            if ans[i] == p:
                if i == len(ans)-1:
                    return None
                else:
                    return ans[i+1]
                
                
    
    def helper(self, root, ans):
        if not root:
            return
        self.helper(root.left, ans)
        ans.append(root)
        
        self.helper(root.right, ans)
        
        