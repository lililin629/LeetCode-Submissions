class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = [] # for '()'
        to_rm = set() # for idx to be reomoved
        string_builder = []
        
        for i in range(len(s)):
            if s[i] not in '()':
                continue
            elif s[i] == '(':
                st.append(i)
            elif s[i] == ')' and not st:
                # right paren appears first
                to_rm.add(i)
            elif s[i] == ')':
                st.pop()
        to_rm = to_rm.union(set(st))
        for i in range(len(s)):
            if i not in to_rm:
                string_builder.append(s[i])
        return ''.join(string_builder)
                
                
        