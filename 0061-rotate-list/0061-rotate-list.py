# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        
        counter = 1
       
        #old tail
        cur = head
        while cur.next:
            cur = cur.next
            counter += 1
        cur.next = head
        
        k = k% counter
        
        target = counter - k -1
        
        #new tail
        cur2 = head
        for i in range(target):
            cur2 = cur2.next
        new_head = cur2.next
        cur2.next = None
        
        
        return new_head
            
                
        
        