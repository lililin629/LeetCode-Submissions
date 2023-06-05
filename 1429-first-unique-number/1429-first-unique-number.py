class Node:
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None

class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dummy = Node(0)
        self.tail = self.dummy
        self.numToNode = {}
        self.duplicate = set() 
        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        """
        :rtype: int
        """
        if self.dummy.next:
            return self.dummy.next.val
        else:
            return -1
        
    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value in self.duplicate:
            return
        if value in self.numToNode:
            self.remove(value)
            self.duplicate.add(value)
            return
        self.add_to_tail(value)
    
    def remove(self, value):
        node = self.numToNode.get(value)
        prev = node.prev
        prev.next = node.next
        if node.next:
            node.next.prev = prev
        else:
            self.tail = prev
        self.numToNode.pop(value)
        
    
    def add_to_tail(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
        self.numToNode[value] = newNode
        
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)