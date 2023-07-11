class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        s = set(['+','-','*','/'])
        for t in tokens:
            if t not in s:
                t = int(t)
                stack.append(t)
        
            else:
                o1 = stack.pop()
                o2 = stack.pop()
                if t == '+':
                    r = o2 + o1
                    stack.append(r)
                if t == '-':
                    r = o2 - o1
                    stack.append(r)
                if t == '*':
                    r = o2 * o1
                    stack.append(r) 
                if t == '/':
                    r = int(o2 / o1)
                    stack.append(r) 
        return stack[0]
        