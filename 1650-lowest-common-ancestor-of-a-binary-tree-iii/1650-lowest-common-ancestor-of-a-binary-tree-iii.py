"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

# sol1: set
# class Solution:
#     def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
#         if not q or not p:
#             return None
#         parent_set = set()
#         cur = p
#         while cur is not None:
#             parent_set.add(cur)
#             cur = cur.parent
        
#         cur = q
#         while cur is not None:
#             if cur in parent_set:
#                 return cur
#             cur = cur.parent


# sol2: list
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        if not q or not p:
            return None
        list_p = self.parent_list(p)
        list_q = self.parent_list(q)
        
        lca = None
        while len(list_p) > 0 and len(list_q) > 0:
            a = list_p.pop()
            b = list_q.pop()
            if a == b:
                lca = a
        return lca
    
    
    def parent_list(self, node):
        list_node = []
        cur = node
        while cur is not None:
            list_node.append(cur)
            cur = cur.parent
        return list_node
        
        
        
        