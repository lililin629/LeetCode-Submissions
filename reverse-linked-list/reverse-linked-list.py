# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur = head
        new_tail = cur.next
        new_head = self.reverseList(head.next)
        new_tail.next = cur
        cur.next = None
        
        return new_head
        
        
        