"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque([root])
        
        while q:
            lev = len(q)
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            for _ in range(lev-1):
                nex = q.popleft()
                node.next = nex
                node = nex
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
            
                
            
        