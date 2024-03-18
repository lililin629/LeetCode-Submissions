# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)
        self.dfs(root, ans)
        # change to list
        ans_lst = []
        for key in ans:
            ans_lst.append(ans[key])
        return ans_lst
    
    def dfs(self, root, ans):
        if not root:
            return 0
        if not root.left and not root.right:
            ans[0].append(root.val)
            return 1
        l_lev = self.dfs(root.left, ans)
        r_lev = self.dfs(root.right, ans)
        lev = max(l_lev, r_lev)
        ans[lev].append(root.val)
        
        return lev+1
        
        