class TwoSum:

    def __init__(self):
        self.ls = []
        

    def add(self, number: int) -> None:
        self.ls.append(number)
        

    def find(self, value: int) -> bool:
        self.ls.sort()
        f = 0
        e = len(self.ls) - 1
        while f < e:
            if self.ls[f] + self.ls[e] == value:
                return True
            else:
                if self.ls[f] + self.ls[e] > value:
                    e -= 1
                else:
                    f += 1
        return False
        
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)