# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.helper(1, n)
    
    @lru_cache
    def helper(self, start, end):
        if start > end:
            return [None]
        ans = []
        for i in range(start, end+1):
            lefts = self.helper(start, i-1)
            rights = self.helper(i+1, end)
            
            for l in lefts:
                for r in rights:
                    ans.append(TreeNode(i, l, r))
        return ans
        