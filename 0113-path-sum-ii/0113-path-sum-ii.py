# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        self.dfs(root, targetSum, [])
        return self.ans

        
    def dfs(self, root, targetSum, curList):
        if not root:
            return
        
        curList.append(root.val)
        
        if not root.left and not root.right:
            if sum(curList) == targetSum:
                self.ans.append(list(curList))
            
        else:
            self.dfs(root.left, targetSum, curList)
            self.dfs(root.right, targetSum, curList)
        
        curList.pop()
        
        