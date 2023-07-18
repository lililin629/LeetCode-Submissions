# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dic = {} #{-1: [9], 0:[3, 15],...}
        q = deque([(root, 0)])
        
        while q:
            cur, col = q.popleft()
            if col not in dic:
                dic[col] = [cur.val]
            else:
                dic[col].append(cur.val)
                
            if cur.left:
                q.append((cur.left, col-1))
            if cur.right:
                q.append((cur.right, col+1))
        ans = []    
        dic = dict(sorted(dic.items()))
        for key in dic:
            ans.append(dic[key])
        return ans
            
                
                
                
        
        