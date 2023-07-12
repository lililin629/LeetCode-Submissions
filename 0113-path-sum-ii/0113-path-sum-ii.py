# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        
        def helper(root, targetSum, ls):
            if not root:
                return 
            
            ls.append(root.val)
            
            if not root.left and not root.right:
                if root.val == targetSum:
                    ans.append(list(ls))
               

            helper(root.left, targetSum - root.val, ls) 
            helper(root.right, targetSum - root.val, ls)
            ls.pop()
            
            return ans
        
        return helper(root, targetSum, [])
            
        