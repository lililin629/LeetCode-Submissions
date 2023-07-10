# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = {}
        ret = []
        
        def dfs(root): # returns (height, val)
            if not root:
                return -1, 0
            else:
                lh, l = dfs(root.left)
                rh, r = dfs(root.right)
                h, v = max(lh, rh)+1, root.val
                if h not in ans:
                    ans[h] = [v]
                else:
                    ans[h].append(v)
                return h, v
            
        dfs(root)
        sorted(ans.items())
        
        for h in ans:
            ret.append(ans[h])
            
        return ret
                    
        