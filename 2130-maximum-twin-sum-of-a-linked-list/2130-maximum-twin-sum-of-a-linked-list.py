# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # reverse the second half (O(1) space complexity)
        # 快慢指針找到中點
        
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse second half
        pre = None
        cur = slow
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        head2 = pre
        
        # 2 pointers
        p1 = head
        p2 = head2
        maxv = 0
        while p1 and p2:
            maxv = max(p1.val+p2.val, maxv)
            p1 = p1.next
            p2 = p2.next
        
        return maxv
        
        
        
            
        
        
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
        
#         ls = []
#         cur = head
        
#         while cur:
#             ls.append(cur.val)
#             cur = cur.next
        
#         l = 0
#         r = len(ls) - 1
        
#         max_ans = 0
#         while l < r:
#             max_ans = max(max_ans, ls[l]+ls[r])
#             l += 1
#             r -= 1
        
        
#         return max_ans
            
        