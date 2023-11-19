# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find mid point
        fast = head
        slow = head
       
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        # reverse second half
        rev = self.reverseList(mid)
        # join 2 lists
        
        cur1 = head
        cur2 = rev
        
        while cur1 and cur2:
            # Save next nodes
            temp1 = cur1.next
            temp2 = cur2.next

            # Link cur1 to cur2
            cur1.next = cur2

            # Move cur1 to its original next
            cur1 = temp1

            # Link cur2 to the next of cur1
            cur2.next = cur1

            # Move cur2 to its original next
            cur2 = temp2

            
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        new_tail = head.next
        new_head = self.reverseList(head.next)
        new_tail.next = head
        head.next = None
        
        return new_head