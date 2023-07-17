# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = TreeNode(float('-inf'))
        high = None
        low = None

        def find_nodes(root):
            nonlocal prev, high, low
            if not root:
                return
            find_nodes(root.left)
            if prev.val > root.val:
                if not high:
                    high = prev
                low = root
            prev = root
            find_nodes(root.right)
            return high, low
        
        h, l = find_nodes(root)
        h.val, l.val = l.val, h.val
           
# class Solution:
#     def recoverTree(self, root: Optional[TreeNode]) -> None:
#         """
#         Do not return anything, modify root in-place instead.
        
#         """
        
        # dummy = TreeNode(float('-inf'))
        # seq = [dummy]
        # def find_nodes(root):
        #     # left, root, right
        #     if not root:
        #         return 
        #     find_nodes(root.left)
        #     if root.val > seq[-1].val:
        #         seq.append(root)
        #     else:
        #         return (seq[-1], root)
        #     find_nodes(root.right)


        # def rotate_nodes(a, b):
        #     temp = a.val
        #     a.val = b.val
        #     b.val = temp
        
        # a, b = find_nodes(root)
        # rotate_nodes(a, b)
        

