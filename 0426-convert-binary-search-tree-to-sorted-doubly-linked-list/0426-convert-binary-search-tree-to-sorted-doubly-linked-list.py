"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        # the smallest (first) and the largest (last) nodes
        self.first, self.last = None, None
        self.helper(root)
        # close DLL
        self.last.right = self.first
        self.first.left = self.last
        return self.first
    
    def helper(self, node):
            """
            Performs standard inorder traversal:
            left -> node -> right
            and links all nodes into DLL
            """
            if not node:
                return
            
            # left
            self.helper(node.left)
            # node 
            if self.last:
                # link the previous node (last)
                # with the current one (node)
                self.last.right = node
                node.left = self.last
            else:
                # keep the smallest node
                # to close DLL later on
                self.first = node        
            self.last = node
            # right
            self.helper(node.right)