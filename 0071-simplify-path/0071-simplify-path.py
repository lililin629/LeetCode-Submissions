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
                   
                
        