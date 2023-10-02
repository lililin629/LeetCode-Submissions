# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        
        dummy = head
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        extra = length % k # 10%3 = 1 # 3%5 = 3
        num = length // k # 10//3 = 3 # 3//5 = 0
        
        lens = []
        for _ in range(k):
            if extra > 0:
                lens.append(num+1)
                extra -= 1
            else:
                lens.append(num)
        
        ans = []
        cur = head
        
        for le in lens:
            if not le:
                ans.append(None)
            else:
                ans.append(cur)
                for _ in range(le-1):
                    cur = cur.next
                temp = cur.next
                cur.next = None
                cur = temp
        return ans
                
                
                
            
            
            

         
                
                
            
        