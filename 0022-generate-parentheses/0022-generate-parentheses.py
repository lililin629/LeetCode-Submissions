class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        
        def is_valid(s):
            stack = []
            if len(s)%2 == 1:
                return False
            for ch in s:
                if ch == ')':
                    if stack:
                        if stack.pop() == '(':
                            continue
                        else:
                            return False
                stack.append(ch)
            if not stack:
                return True
            return False
                
            
        def helper(s):
            
            if len(s) == 2*n:
                if is_valid(s):
                    ans.append(s)
                return 
                
            helper(s+'(')
            helper(s+')')
        
        helper('')    
        return ans

    
    

        
            
        