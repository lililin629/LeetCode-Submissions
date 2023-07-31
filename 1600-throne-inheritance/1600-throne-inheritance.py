class ThroneInheritance:

    def __init__(self, kingName: str):
        self.children = defaultdict(list)
        self.name = kingName
        self.dead = set()
        
       

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.dead.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        # {bob:[a, b c], a:[d], b:[e]}
        # [bob, a, d, b, e, c]
        order = []
        self.helper(self.name, order)
        return order

    def helper(self, name, order):
        if name not in self.dead:
            order.append(name)
        for c in self.children[name]:
            self.helper(c, order)
        
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()