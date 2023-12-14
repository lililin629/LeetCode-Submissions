# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        q = deque([root])
        s = []
        while q:
            node = q.popleft()
            if node:
                s.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                s.append('n')
        st = ','.join(s)
        return st
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        lst = data.split(',')
        
        
        num = lst[0]
        root = TreeNode(int(num))
        nq = deque([root])
       
        
        if len(lst) > 1:    
            q = deque(lst[1:])

        
        while nq:
            node = nq.popleft()
            if q:
                l_val = q.popleft()
            
            if l_val != 'n':
                lnode = TreeNode(int(l_val))
                nq.append(lnode)
                node.left = lnode
            else:
                node.left = None
            
            if q:
                r_val = q.popleft()
            
            if r_val != 'n':
                rnode = TreeNode(int(r_val))
                nq.append(rnode)
                node.right = rnode
            else:
                node.right = None
        return root
            
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))