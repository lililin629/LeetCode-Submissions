# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        cache = {}
        return self.helper(1, n, cache)
    
    
    def helper(self, start, end, cache):
        if (start, end) in cache:
            return cache[(start, end)]
        if start > end:
            return [None]
        if start == end:
            return [TreeNode(start)]
        ans = []
        for i in range(start, end+1):
            lefts = self.helper(start, i-1, cache)
            rights = self.helper(i+1, end, cache)
            
            for l in lefts:
                for r in rights:
                    ans.append(TreeNode(i, l, r))
                    cache[(start, end)] = ans
        return ans
        