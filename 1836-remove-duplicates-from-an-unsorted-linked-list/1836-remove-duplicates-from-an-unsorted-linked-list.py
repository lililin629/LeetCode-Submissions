# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicatesUnsorted(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        cur2 = dummy

        s = {}
        while cur:
            s[cur.val] = s.get(cur.val, 0) + 1
            cur = cur.next
       

        while cur2.next:
            if s[cur2.next.val] > 1:
                cur2.next = cur2.next.next
            else:
                cur2 = cur2.next
        return dummy.next
        # return head # is wrong # why

        
        


