class Solution:
    def calculate(self, s: str) -> int:
        
        st = []
        temp = ''
        for i in range(len(s)):
            ch = s[i]
            # [1, -, (, -, 2]
            if ch == ')':
                
                while st[-1] is not '(':
                    # print(st)
                    temp = st.pop() + temp
                    # print('temp')
                    # print(temp)
                st.pop() # pop'('
                calculated = self.calc(temp)
                temp = ''
                # print('calc')
                # print(calculated)
                if i == len(s)-1 and not st:
                    return calculated
                else:
                    num_str = str(calculated)
                    # print('numstr')
                    # print(num_str)
                    for c in num_str:
                        st.append(c)
                    # print(st)
            elif ch == ' ':
                continue
            else:
                st.append(ch)
        
        if st:
            while st:
                temp = st.pop() + temp
            # print(temp)
            return self.calc(temp)
    
    def calc(self, t):
        # print(t)
        t += '*'
        ans = 0
        if t[0].isnumeric():
            t = '+' + t
        sign_st = []
        
        num_str = ''
        num = 0
        for ch in t:
            if ch.isdigit():
                num_str += ch
            
            else:
                sign = ''
                if num_str:
                    num = int(num_str)
                    
                    while sign_st:
                        sign = sign_st.pop() + sign
                    if sign == '-' or sign == '+-':
                        ans -= num
                    if sign == '+' or sign == '--':
                        ans += num
                # print(sign)
                # print(num)
                if ch == '-' or ch =='+':
                    sign_st.append(ch)
                num_str = ''
                num = 0
       
        return ans
                
                
        
        
        
        
                
                
