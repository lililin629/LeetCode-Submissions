# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        s = head
        f = head
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
        if f.next:
            return s.next
        return s