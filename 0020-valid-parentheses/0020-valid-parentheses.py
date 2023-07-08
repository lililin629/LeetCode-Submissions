class Solution:
    def isValid(self, s: str) -> bool:
        # {[()]}
        # {(}
        
        def is_a_pair(p1, p2):
            if p1 == '(':
                if p2 == ')':
                    return True
            if p1 == '{':
                if p2 == '}':
                    return True
            if p1 == '[':
                if p2 == ']':
                    return True
            return False
                
        
        stack = []
        
        for p in s:
            if stack and is_a_pair(stack[-1], p):
                    stack.pop(-1)
            else:
                stack.append(p)
        if not stack:
            return True
        return False
                
       
            
        