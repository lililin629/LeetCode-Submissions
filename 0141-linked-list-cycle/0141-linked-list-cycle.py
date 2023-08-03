# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        cur = head
        
        while cur:
            if cur.val == 10**6:
                return True
            
            cur.val = 10**6
            cur = cur.next
            
            
            
#         s = set()
        
#         while cur:
#             if cur in s:
#                 return True
#             else:
#                 s.add(cur)
#             cur = cur.next
#         return False
        
        
        
        