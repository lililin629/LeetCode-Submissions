class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # Maps keys to Node objects
        self.left = Node(0, 0)  # Left (oldest) sentinel node
        self.right = Node(0, 0)  # Right (most recent) sentinel node
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node):
        """Remove a node from the linked list."""
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _insert(self, node):
        """Insert a node to the right (most recent) end of the linked list."""
        prev = self.right.prev
        next = self.right
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.cap:
            # Remove from the linked list and delete the LRU from the cache
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]

