"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        # Find all nodes
        nodes = self.find_nodes(node)
        # Map all nodes
        mapping = self.map_nodes(nodes)
        # Map all edges
        self.map_edges(mapping)
        return mapping[node]
        
        
    def find_nodes(self, node):
        queue = collections.deque([node])
        visited = set([node])
        while queue:
            cur_node = queue.popleft()
            for neighbor in cur_node.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
        return visited
    
    
    def map_nodes(self, nodes):
        mapping = {}
        for node in nodes:
            mapping[node] = Node(node.val)
        return mapping
    
    
    def map_edges(self, mapping):
        for node in mapping:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
            
