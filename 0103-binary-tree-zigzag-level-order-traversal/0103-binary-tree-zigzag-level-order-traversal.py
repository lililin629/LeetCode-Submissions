# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        next_q = deque([(root, 0)])
        if not root:
            return ans
        
        while next_q:
            cur_lst = []
            cur_q = next_q
            next_q = deque()
            r, lev = cur_q[0]
            
            while cur_q:
                r, lev = cur_q.popleft()
                cur_lst.append(r.val)
                    
                if r.left:
                    next_q.append((r.left, lev+1))
                if r.right:
                    next_q.append((r.right, lev+1))
                
            # if level is odd: right to left
            if lev % 2 != 0:
                cur_lst.reverse()
                    
            ans.append(cur_lst)
        return ans
        
        
                
                
        