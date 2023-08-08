"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        
        self.diameter = 0
        
        
        self.dfs(root)
        
        return self.diameter
    
    
    def dfs(self, root):
        long1 = 0
        long2 = 0
        if not root.children:
            return 0
        
        for child in root.children:
            cur = self.dfs(child) + 1
            if cur > long1:
                long1, long2 = cur, long1
            elif cur > long2:
                long2 = cur
        self.diameter = max(self.diameter, long1+long2)
        return long1
        
            
            
            