class Solution:
    def isValid(self, s: str) -> bool:
        # (({}))
        
        # {}(())
        
        # {(})
        
        # {)
        
        st = []
        left = {'(', '{', '['}
        pair = {')':'(', '}':'{', ']':'['}
        
        for br in s:
            if br in left:
                st.append(br)
            else:
                if st and st[-1] == pair[br]:
                    st.pop()
                else:
                    return False
        if not st:
            return True
        return False
                
        
                
                
        
        
        
        
        
