class TwoSum:

    def __init__(self):
        self.d = defaultdict(int)
        

    def add(self, number: int) -> None:
        self.d[number] += 1
        

    def find(self, value: int) -> bool:
        for i in self.d:
            if value-i == i:
                if self.d[i] > 1:
                    return True
                continue
            if value-i in self.d:
                return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)