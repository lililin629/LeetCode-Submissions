"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        if not q or not p:
            return None
        parent_set = set()
        cur = p
        while cur is not None:
            parent_set.add(cur)
            cur = cur.parent
        
        cur = q
        while cur is not None:
            if cur in parent_set:
                return cur
            cur = cur.parent
        
        