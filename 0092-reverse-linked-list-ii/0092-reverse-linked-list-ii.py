# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # LL
        ll = dummy
        l = head
        for i in range(left-1):
            ll = ll.next
            l = l.next
        
        # reverse
        # LL.next = new head
        # new tail.next = RR
        pre = None
        cur = l
        
        for i in range(right-left+1):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        l.next = cur
        ll.next = pre
        return dummy.next
        
        
            
            
        