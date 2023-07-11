# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.cur = -1
        self.ls = self.dfs(root, [])
        

    def next(self) -> int:
        self.cur += 1
        return self.ls[self.cur]  
        

    def hasNext(self) -> bool:
        if self.cur == len(self.ls)-1:
            return False
        return True
        
    
    def dfs(self, root, ls):
        if root:
            self.dfs(root.left, ls)
            ls.append(root.val)
            self.dfs(root.right, ls)
        return ls
        
        
            
            
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()