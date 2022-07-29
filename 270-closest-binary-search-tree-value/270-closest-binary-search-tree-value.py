# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# sol1: divide and conquer
# class Solution:
#     def closestValue(self, root: Optional[TreeNode], target: float) -> int:
#         # recursion
#         # find upper, lower bounds and return the bound closer to target
#         if not root:
#             return None
        
#         upper_bound = self.find_upper(root, target)
#         lower_bound = self.find_lower(root, target)
        
#         if upper_bound is None:
#             return lower_bound
        
#         if lower_bound is None:
#             return upper_bound
        
#         return upper_bound if abs(upper_bound - target) < abs(lower_bound - target) else lower_bound
    

#     def find_upper(self, root: TreeNode, target: float) -> int:
#         if not root:
#             return None
#         if root.val <= target:
#             return self.find_upper(root.right, target)
#         closer_up = self.find_upper(root.left, target)
#         return closer_up if closer_up is not None else root.val
    
    
#     def find_lower(self, root: TreeNode, target: float) -> int:
#         if not root:
#             return None
#         if root.val > target:
#             return self.find_lower(root.left, target)
#         closer_low = self.find_lower(root.right, target)
#         return closer_low if closer_low is not None else root.val


# sol2: non-recursive, 3 pointers
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        lower = None
        upper = None
        while root:
            if root.val < target:
                lower = root
                root = root.right
            elif root.val > target:
                upper = root
                root = root.left
            else:
                return root.val
            
        if not upper:
            return lower.val
        elif not lower:
            return upper.val
        else:
            return lower.val if abs(lower.val-target) < abs(upper.val-target) else upper.val
            
        