# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = head.next
        cur = head.next.next
        el = head.next
        ol = head
        odd = True
        while cur:
            if odd:
                ol.next = cur
                ol = cur
                odd = False
            else:
                el.next = cur
                el = cur
                odd = True
            cur = cur.next
        if odd:
            ol.next = None
        else:
            el.next = None

        ol.next = temp
        print(head)
        return head

            

            

            
            
        