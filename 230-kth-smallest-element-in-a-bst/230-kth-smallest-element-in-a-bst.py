# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # queue
        # path to leftest child
        q = []
        self.to_leftest(root, q)
        
        for i in range(k-1): 
            # 0->(k-2) aka 1->(k-1) elements will be popped, leaving the kth element in top of q
            node = q.pop()
            if node.right:
                self.to_leftest(node.right, q)
        return q[-1].val
    
    def to_leftest(self, node, q):
        while node is not None:
            q.append(node)
            node = node.left
            
                
        