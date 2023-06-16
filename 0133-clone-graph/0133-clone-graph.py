"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

    
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        if node.neighbors == []:
            return Node(node.val, None) 
        
        # created placeholder map val->new_nodes
        queue = deque([node])
        clones = {}
        while queue:
            og = queue.popleft()
            for nei in og.neighbors:
                if nei.val not in clones:
                    clone = Node(nei.val, [])
                    clones[nei.val] = clone
                    queue.append(nei)
                    
                
        # add neighbors to things in map
        queue = deque([node])
        visited = set([node.val])
        while queue:
            og = queue.popleft()
            
            for nei in og.neighbors:
                clones[og.val].neighbors.append(clones[nei.val])
                if nei.val not in visited:
                    visited.add(nei.val)
                    queue.append(nei)
       
        return clones[node.val]
                    
                    
        
