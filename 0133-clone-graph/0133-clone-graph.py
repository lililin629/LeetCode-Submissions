"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        q = deque([node])
        ans = dict()
        ans[node] = Node(node.val, [])
        
        while q:
            nx = q.popleft()
            for nei in nx.neighbors:
                if nei not in ans:
                    q.append(nei)
                    ans[nei] = Node(nei.val, [])
                ans[nx].neighbors.append(ans[nei])
        return ans[node]
            
        
            
        
        