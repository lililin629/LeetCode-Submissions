# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # get length 
        # find the 2 nodes
        # swap
        
        cur = head
        l = 0
        while cur:
            l += 1
            cur = cur.next
        
        cur = head
        n1 = None
        n2 = None
        step = 0
        while cur:
            step += 1
            if step == k:
                n1 = cur
                
            if step == (l-k+1):
                n2 = cur
               
            cur = cur.next
        
        
        n1.val, n2.val = n2.val, n1.val
        return head
                
                
            