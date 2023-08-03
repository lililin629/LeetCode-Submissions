# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        n1 = self.num(l1)
        n2 = self.num(l2)
        
        n3 = n1 + n2 # 807
        new = ListNode(n3%10)
        cur = new
        while n3 >= 10:
            n3 //= 10 
            cur.next = ListNode(n3%10)
            cur = cur.next
            
        return new
            
            
        
        
        
    def num(self, l):
        cur = l
        n = 0
        power = 0
        while cur:
            n += cur.val*10**power
            power += 1
            cur = cur.next
        return n
            
            
            
        