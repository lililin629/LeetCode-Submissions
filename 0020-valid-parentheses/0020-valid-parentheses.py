class Solution:
    def isValid(self, s: str) -> bool:
        self.st = []
        # FILO
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                self.st.append(ch)
            if ch == ')':
                if self.check(ch, '('):
                    continue
                return False
            if ch == ']':
                if self.check(ch, '['):
                    continue
                return False
            if ch == '}':
                if self.check(ch, '{'):
                    continue
                return False
                
            
        if len(self.st) != 0:
            return False
        return True
    
    def check(self, ch, lp):
        if self.st and self.st[-1] == lp:
            self.st.pop()
            return True
        return False
        
            
                
            
        