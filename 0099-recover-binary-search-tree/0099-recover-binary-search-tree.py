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
#         prev = None
#         nodes = []
        
#         def find_nodes(prev, root):
#             if not root:
#                 return
#             # left mid right
#             find_nodes(prev, root.left)
#             if prev.val > root.val:
#                 nodes.append(root)
#             prev = root
#             find_nodes(prev, root.right)
        
#         find_nodes(prev, root)
#         nodes[0].val, nodes[1].val = nodes[1].val, nodes[0].val
            
  
        
#         prev = TreeNode(float('-inf'))
#         high = None
#         low = None

#         def find_nodes(root):
#             nonlocal prev, high, low
#             if not root:
#                 return
#             find_nodes(root.left)
#             if prev.val > root.val:
#                 if not high:
#                     high = prev
#                 low = root
#             prev = root
#             find_nodes(root.right)
#             return high, low
        
#         h, l = find_nodes(root)
#         h.val, l.val = l.val, h.val
           
# class Solution:
#     def recoverTree(self, root: Optional[TreeNode]) -> None:
#         """
#         Do not return anything, modify root in-place instead.
        
#         """
        
        dummy = TreeNode(float('-inf'))
        seq = [dummy]
        high = None
        low = None
        
        def find_nodes(root):
            nonlocal high, low
            # left, root, right
            if not root:
                return 
            find_nodes(root.left)
            if root.val < seq[-1].val:
                if not high:
                    high = seq[-1]
                low = root
            seq.append(root)
        
            find_nodes(root.right)


        def rotate_nodes(a, b):
            temp = a.val
            a.val = b.val
            b.val = temp
        
        find_nodes(root)
        print(low, high)
        rotate_nodes(low, high)
        

