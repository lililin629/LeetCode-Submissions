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
        d = dict()
        cur = head
        new_head = Node(cur.val)
        d[head] = new_head
        
        
        cur2 = new_head
        cur = cur.next
       
        while cur:
            if cur in d:
                new = d[cur]
            else:
                new = Node(cur.val)
            d[cur] = new
            cur2.next = new
            cur2 = cur2.next
            cur = cur.next
    
        cur = head
        cur2 = new_head
        while cur and cur2:
            if cur.random == None:
                cur2.random = None
            else:
                cur2.random = d[cur.random]
            
            cur2 = cur2.next
            cur = cur.next
        return new_head
            
       
            
        
            
            
        
        