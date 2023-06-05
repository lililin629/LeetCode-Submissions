import random 

class RandomizedSet(object):

    def __init__(self):
        self.ls = []
        self.dict = {}
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            return False
        ind = len(self.ls)
        self.ls.append(val)
        self.dict[val] = ind
        return True


    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            return False
        ind =  self.dict[val]
        if ind < len(self.ls)-1:
            last = self.ls[len(self.ls)-1]
            self.ls[ind] = last
            self.dict[last] = ind
        
        self.ls.pop()
        self.dict.pop(val)
        return True

        

    def getRandom(self):
        """
        :rtype: int
        """
        return self.ls[random.randint(0, len(self.ls)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()