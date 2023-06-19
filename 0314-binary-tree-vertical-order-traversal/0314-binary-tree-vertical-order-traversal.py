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
        dic = {root: 0} # {node: node.x}
        xdic = {} #{x:[node.val, ...]}
       
        queue = deque([root])
           
        while queue:
            cur_level = len(queue)
            for i in range(cur_level):
                cur = queue.popleft()
                cur_x = dic[cur]
                if cur_x not in xdic:
                    xdic[cur_x] = [cur.val]
                else:
                    xdic[cur_x].append(cur.val)
                    
                if cur.left:
                    queue.append(cur.left)
                    dic[cur.left] = cur_x - 1
                    
                if cur.right:
                    queue.append(cur.right)
                    dic[cur.right] = cur_x + 1
        sorted_dict = dict(sorted(xdic.items()))
        ans = []
        for x in sorted_dict:
            ans.append(sorted_dict[x])
        return ans
            
            
                    

        
            
                
                
            
                
         
            
        
        
        