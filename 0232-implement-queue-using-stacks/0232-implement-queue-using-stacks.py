class MyQueue:

    def __init__(self):
        self.ls1 = []

        
    def push(self, x: int) -> None:
        self.ls1.append(x)
        

    def pop(self) -> int:
        if self.ls1:
            return self.ls1.pop(0)
        

    def peek(self) -> int:
        if self.ls1:
             return self.ls1[0]
        

    def empty(self) -> bool:
        if not self.ls1:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()