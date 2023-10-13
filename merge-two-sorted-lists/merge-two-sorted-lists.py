# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       
        return self.helper(list1, list2)
    
    @cache
    def helper(self, l1, l2):
        # Define a placeholder for the result list
        new = ListNode(0)
        current = new

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            # Move to the next node
            current = current.next

        # At the end of loop, attach the non-empty list
        if l1 is not None:
            current.next = l1
        else:
            current.next = l2

        return new.next
            
            
        
        