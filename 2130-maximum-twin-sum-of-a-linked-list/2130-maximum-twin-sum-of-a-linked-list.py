# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        ls = []
        cur = head
        
        while cur:
            ls.append(cur.val)
            cur = cur.next
        
        l = 0
        r = len(ls) - 1
        
        max_ans = 0
        while l < r:
            max_ans = max(max_ans, ls[l]+ls[r])
            l += 1
            r -= 1
        
        
        return max_ans
            
        