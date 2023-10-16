class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        
        for ch in s:
    
            decoded = ''
            if ch == ']':
                while st[-1] != '[':
                    decoded += st.pop()
                st.pop()
                num = ''
                while st and st[-1].isnumeric():
                    
                    num = st.pop() + num
                num1 = 0
                for n in num:
                    num1 = num1*10 + int(n)
                    
                for _ in range(num1):
                    for c in decoded[::-1]:
                        st.append(c)
            else:
                # push into stack in order
                st.append(ch)
        ans = ''
    
        while st:
            ans = st.pop() + ans
        return ans
            
       
                
            
        