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
        
        slow = head
        fast = head
        
        if not head:
            return head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        # reverse the second half
        # cur = new_tail
        # tmp = None
        # while cur.next and cur.next.next:
        #     prev = cur
        #     cur = cur.next
        #     tmp = cur.next
        #     cur.next = prev
        # new_tail.next = None
        # second_head = tmp
        prev, cur = None, mid
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        second_head = prev
            
        # link nodes from each half alternatingly
        cur = head
        cur2 = second_head
        while cur2.next:
            tmp = cur.next
            cur.next = cur2
            cur = tmp
            
            tmp = cur2.next
            cur2.next = cur
            cur2 = tmp
        return head
        
            
        
        