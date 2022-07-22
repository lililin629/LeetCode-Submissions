# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # write your code here
        stack = []
        pred = float('-inf')
        while stack or root:
            while root:   # while not leaf -> traverse to leftest leaf
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            if pred <= target and target < root.val:
                return min(pred, root.val, key = lambda x: abs(x-target))

            pred = root.val
            root = root.right
        return pred
        
        
        
       
       
        