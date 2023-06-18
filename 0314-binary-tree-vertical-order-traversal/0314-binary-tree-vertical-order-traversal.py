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
        
        
        # depth = 0
        while queue:
            # depth += 1
            cur_level = len(queue)
            for i in range(cur_level):
                cur = queue.popleft()
                # dic[cur][1] = depth
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
            
            
                    
#         new_dic = {} #{x:[node.val, ...]}
#         for node in dic:
#             x = dic[node]
           
#             if x not in new_dic:
#                 new_dic[x] = [(depth, node.val)]
#             else:
#                 new_dic[x].append((depth, node.val))
            
#         sorted_dict = dict(sorted(new_dic.items()))
#         ans = []
#         for key in sorted_dict:
#             sorted_dict[key].sort()
#             lst = []
#             for item in sorted_dict[key]:
#                 lst.append(item[1])
#             ans.append(lst)
#         return ans
        
            
                
                
            
                
         
            
        
        
        