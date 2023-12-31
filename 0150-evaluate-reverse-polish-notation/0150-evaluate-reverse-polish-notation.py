class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        
        for tok in tokens:
            # print(stk)
            if tok.lstrip('-').isdigit():
                stk.append(int(tok))
            else:
                right = stk.pop()
                left = stk.pop()
                if tok == "+":
                    stk.append(left+right)
                if tok == "-":
                    stk.append(left-right)
                if tok == "*":
                    stk.append(left*right)
                if tok == "/":
                    stk.append(int(left/right))
            
        return stk[0]
                
                    
        