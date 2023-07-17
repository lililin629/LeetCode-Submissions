# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        if len(nums) == 1:
            return TreeNode(nums[0])
        idx, max_val = self.find_max(nums)
        root = TreeNode(max_val)
        if idx > 0:
            root.left = self.constructMaximumBinaryTree(nums[:idx])
        if idx < len(nums)-1:
            root.right = self.constructMaximumBinaryTree(nums[idx + 1:])
        return root
    
    def find_max(self, nums):
        max_v = -1
        max_i = -1
        for i in range(len(nums)):
            if nums[i] > max_v:
                max_i = i
                max_v = nums[i]
        return max_i, max_v
                
    
            
        
        