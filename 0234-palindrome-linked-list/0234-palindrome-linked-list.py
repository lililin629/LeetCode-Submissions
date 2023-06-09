# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        # reverse linked list
        cur = head
        v = []
        while cur:
            v.append(cur.val)
            cur = cur.next
        

        # loop over 2 lists to compare
        i = len(v)-1
        for j in range(i):
            val0 = v[j]
            val1 = v[i]
            i -= 1
            if val0 != val1:
                return False
        return True
        