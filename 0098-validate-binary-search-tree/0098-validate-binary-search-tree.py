# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # (left, root, right) traversal -> ls1
        # ls2 = sorted(ls1)
        # if ls1 == ls2: return True
        
        ls1 = []
        def dfs(root):
            if not root:
                return
            else:
                dfs(root.left)
                ls1.append(root.val)
                dfs(root.right)
        
        dfs(root)
        ls2 = sorted(ls1)
        s1 = set(ls1)
        
        
        if ls1 == ls2 and len(s1) == len(ls1):
            return True
        else:
            return False
       
        
        