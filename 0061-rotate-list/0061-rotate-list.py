# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        l = 0
        cur = head
        while cur:
            cur = cur.next
            l += 1
            
        if l == 0 or l == 1:
            return head
        
        k %= l
        
        if k == 0:
            return head
        
        d = ListNode()
        d.next = head
        f = d 
        s = d
        
        for _ in range(k):
            f = f.next
        
        while f.next:
            f = f.next
            s = s.next
        
        d.next = s.next
        f.next = head
        s.next = None
        
        return d.next
        
        
        
        