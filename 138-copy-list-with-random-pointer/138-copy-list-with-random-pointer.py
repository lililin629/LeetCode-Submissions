"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # find nodes 
        nodes = self.find_nodes(head)
        # copy nodes -> {old: new}
        mapping_dict = self.copy_nodes(nodes)
        # copy random pointers
        self.copy_pointers(mapping_dict)
        return mapping_dict[head]
    
    def find_nodes(self, head):
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        return nodes
        
    def copy_nodes(self, nodes):
        mapping_dict = {}
        for node in nodes:
            mapping_dict[node] = Node(node.val)
        return mapping_dict
    
    
    def copy_pointers(self, mapping_dict):
        for node in mapping_dict:
            new_node = mapping_dict[node]
            if node.next is None:
                new_node.next = None
            else:
                new_node.next = mapping_dict[node.next]
            if node.random is None:
                new_node.random = None
            else:
                new_node.random = mapping_dict[node.random]
        