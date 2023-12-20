# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         if path[-1] == "/":
#             path = path[:-1]
#         if path[0] != "/":
#             path = "/"+ path
        
#         st = []
#         for i in range(len(path)):
#             print(st)
#             if path[i] == "/":
#                 if not st or st[-1] != "/":
#                     st.append(path[i])
#             elif path[i] == ".":
#                 if i > 0 and path[i-1] == ".":
#                     times = 2
#                     while st and times:
#                         st.pop()
#                         times -= 1
#             else:
#                 st.append(path[i])
#         ans = "".join(st)
        
#         return ans
            
class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []

        for part in path.split('/'):
            if part == '..':
                if st:
                    st.pop()
            elif part and part != '.':
                st.append(part)

        return '/' + '/'.join(st)
                   
                
        