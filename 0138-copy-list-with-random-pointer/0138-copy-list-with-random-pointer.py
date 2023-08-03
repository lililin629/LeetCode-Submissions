"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        new = Node(head.val)
        
        cur = head
        new_cur = new
        d = dict()
        nd = dict()
        idx = 0
        
        while cur:
            d[cur] = idx
            nd[idx] = new_cur
            
            idx += 1
            
            if cur.next:
                new_cur.next = Node(cur.next.val)
            
            cur = cur.next
            new_cur = new_cur.next
        
        cur = head
        new_cur = new
        
        while cur:
            if cur.random:
                key = d[cur.random]
                new_cur.random = nd[key]
            else:
                new_cur.random = None
            cur = cur.next
            new_cur = new_cur.next
        
        return new
        
        
            
            
            
        