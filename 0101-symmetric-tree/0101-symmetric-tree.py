# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # BST by level
        # get a list for each level
        # check if the list is palindromic
        
        q = deque([root])
        
        
        while q:
            ls = []
            for _ in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                    ls.append(node.left.val)
                else:
                    ls.append(-101)
                
                if node.right:
                    q.append(node.right)
                    ls.append(node.right.val)
                else:
                    ls.append(-101)
               
                
            if not self.isPalin(ls):
                return False
        return True
    
    def isPalin(self, ls):
        p1 = 0
        p2 = len(ls)-1
        while p1 < p2:
            if ls[p1] != ls[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True
    
    
    ##########NOTE#############
    #leaf.left = None
    #None.left 會報錯
                
        