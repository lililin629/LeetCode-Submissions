class LinkedNode:
    def __init__(self, key, val):
        self.key = key
        self. val = val
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.dict = {} # {(key: node)}
        self.dummy = LinkedNode(0,0) 
        self.tail = self.dummy
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # if key not in cache
        if key not in self.dict:
            return -1
        # if key in cache
        else:
            val = self.dict[key].val
            # move node to end
            self.kick(key)
            
            # return val
            return val
    
    def kick(self, key):
        keyNode = self.dict[key]
        prev = keyNode.prev
        if not keyNode.next:
            return
        prev.next = keyNode.next
        keyNode.next = None
        self.tail.next = keyNode
        keyNode.prev = self.tail
        prev.next.prev = prev
        self.tail = keyNode
    

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # if key in dict
        if key in self.dict:
            # update value
            self.dict[key].val = value
            # move to last
            self.kick(key)
        # if key not in dict
        else:
            keyNode = LinkedNode(key, value)
            # if not at capacity
            if len(self.dict) < self.cap:
                # update dict
                self.dict[key] = keyNode
                # add to last
                self.tail.next = keyNode
                keyNode.prev = self.tail
                self.tail = keyNode

            # if at capacity
            else:
                deleted_key = self.dummy.next.key
                if self.dummy.next.next:
                    # replace dummy.next
                    self.dummy.next =  self.dummy.next.next
                    self.dummy.next.prev = self.dummy
                    # add to last
                    self.tail.next = keyNode
                    keyNode.prev = self.tail
                    self.tail = keyNode
                else:
                    # replace dummy.next
                    self.dummy.next = keyNode
                    keyNode.prev = self.dummy
                    self.tail = keyNode
                # update dict
                self.dict.pop(deleted_key)
                self.dict[key] = keyNode




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)