# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.d = defaultdict(int)
        self.d[0] = 1
        self.ans = 0
        self.dfs(root, targetSum, 0)
        return self.ans
    
    def dfs(self, root, targetSum, curSum) -> None:
       
        if not root:
            return
        curSum += root.val
        
        self.ans +=  self.d[curSum - targetSum]
        
        self.d[curSum] += 1
        self.dfs(root.left, targetSum, curSum)
        self.dfs(root.right, targetSum, curSum)
        self.d[curSum] -= 1
        
    
    
        
        
        