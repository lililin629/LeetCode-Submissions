# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # root, left, right
        ls = [] #[[1,2], [1,3]]
        def helper(root, cur_ls):
            if not root:
                return
            cur_ls.append(root.val)
            if not root.left and not root.right:
                ls.append(list(cur_ls))
                cur_ls.pop()
                return
            
            helper(root.left, cur_ls)
            helper(root.right, cur_ls)
            cur_ls.pop()
            
        
        helper(root, [])
        ans = 0
        print(ls)
        for l in ls:
            for i in range(len(l)):
                ans += l[i]*(10**(len(l)-1-i))
        return ans
            
            
            
            
        