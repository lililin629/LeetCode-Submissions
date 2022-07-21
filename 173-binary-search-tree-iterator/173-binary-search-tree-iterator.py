# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.find_most_left(root)
    
    
    def find_most_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    
    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.find_most_left(node.right)
        return node.val
        

    def hasNext(self) -> bool:
        return bool(self.stack)

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()