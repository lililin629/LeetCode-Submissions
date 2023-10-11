# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur = head
        h2 = self.swapPairs(cur.next.next)
        new_head = cur.next
        cur.next.next = cur
        cur.next = h2
        
        return new_head
        