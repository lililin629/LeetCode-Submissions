class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
####################################dfs##########################################
#         ans = []
#         def dfs(cur_s, left, right):
#             if len(cur_s) == 2*n:
#                 ans.append(cur_s)
#             if left < n:
#                 dfs(cur_s+'(', left+1, right)
#             if right < left:
#                 dfs(cur_s+')', left, right+1)
        
#         dfs('', 0, 0)
#         return ans

####################################dfs2#########################################
        def dfs(n):
            ans = set()
            if n == 1:
                return ['()']
            prev = dfs(n-1)
            for p in prev:
                for i in range(len(p)):
                    ans.add(p[:i]+'()'+p[i:])
            return list(ans)
        return dfs(n)   
        # if n == 1:
        #     return ['()']
        # ans = set()
        # for p in self.generateParenthesis(n-1):
        #     for i in range(len(p)):
        #         ans.add(p[:i]+'()'+p[i:])
        # return list(ans)
###################################brute force###################################
#         ans = []
        
#         def is_valid(s):
#             stack = []
#             if len(s)%2 == 1:
#                 return False
#             for ch in s:
#                 if ch == ')':
#                     if stack:
#                         if stack.pop() == '(':
#                             continue
#                         else:
#                             return False
#                 stack.append(ch)
#             if not stack:
#                 return True
#             return False
                
            
#         def helper(s):
            
#             if len(s) == 2*n:
#                 if is_valid(s):
#                     ans.append(s)
#                 return 
                
#             helper(s+'(')
#             helper(s+')')
        
#         helper('')    
#         return ans

    
    

        
            
        