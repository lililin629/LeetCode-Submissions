class MinStack:

    def __init__(self):
        self.insert_order = []
        self.min_stack = []
        self.min = float('inf')
        

    def push(self, val: int) -> None:
        self.insert_order.append(val)
        if val <= self.min:
            self.min_stack.append(self.min)
            self.min = val 
                   

    def pop(self) -> None:
        if self.insert_order[-1] == self.min:
            self.min = self.min_stack.pop()
        self.insert_order = self.insert_order[:-1]
       

    def top(self) -> int:
        return self.insert_order[-1]
        

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()