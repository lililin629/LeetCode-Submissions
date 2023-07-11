# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = {} # {val: count, }
        
        def dfs(root):
            if not root:
                return
            else:
                if root.val not in dic:
                    dic[root.val] = 1
                else:
                    dic[root.val] += 1
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        dic2 = {}
        for v in dic:
            c = dic[v]
            if c not in dic2:
                dic2[c] = [v]
            else:
                dic2[c].append(v)
        dic2 = dict(sorted(dic2.items()))
        
        return dic2.popitem()[1]
            
        