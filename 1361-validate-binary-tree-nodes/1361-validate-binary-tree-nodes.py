class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # no cycle
        # each node (except root) has only 1 parent 
        # all nodes are connected
        visited = set()
        
        q = deque()
        for i in range(n):
            if i not in leftChild and i not in rightChild:
                q.append(i)
                visited.add(i)
        if len(q) > 1:
            return False
        
        while q:
            cur = q.popleft()
            lc = leftChild[cur]
            rc = rightChild[cur]
            if lc != -1:
                if lc in visited:
                    return False
                else:
                    q.append(lc)
                    visited.add(lc)
            if rc != -1:
                if rc in visited:
                    return False
                else:
                    q.append(rc)
                    visited.add(rc)
        
        if len(visited) == n:
            return True
        return False
                
        
        
        