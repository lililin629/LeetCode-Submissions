# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        q = []
        self.to_leftest(root, q)
        lst = []
        while q:
            cur = q.pop()
            lst.append(cur.val)
            if cur.right:
                self.to_leftest(cur.right, q)
        
        if len(lst) <= 1:
            return lst
        return self.find_k_values(lst, target, k)
        
    
    def to_leftest(self, node, q):
        while node:
            q.append(node)
            node = node.left
            
            
    def find_k_values(self, lst, target, k):
        ans = []
        # find the ele closest to target <binary search>
        left = self.find_closest(lst, target)
        right = left + 1
        # 2 pointers
        for _ in range(k):
            if self.left_is_closer(lst, left, right, target):
                ans.append(lst[left])
                left -= 1
            else:
                ans.append(lst[right])
                right += 1
        return ans
        
    
    def left_is_closer(self, lst, left, right, target):
        if left < 0:
            return False
        elif right > len(lst)-1:
            return True
        return abs(lst[left] - target) < abs(lst[right] - target)
        
        
    def find_closest(self, lst, target):
        left = 0
        right = len(lst)-1
        
        while left + 1 < right:
            mid = (left+right) // 2
            if lst[mid] < target:
                left = mid
            elif lst[mid] > target:
                right = mid
            else:
                return mid
        return left
        
        
            
            
            
            
        