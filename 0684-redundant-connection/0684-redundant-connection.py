class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # union find
        d = dict()
        for [n1, n2] in edges:
            if n1 in d and n2 in d:
                head1 = self.getContainingSet(d, n1)
                head2 = self.getContainingSet(d, n2)
                if head1 == head2:
                    return [n1, n2]
                else:
                    d[head1].update(d[head2])
                    for node in d[head2]:
                        d[node] = head1
                    
            elif n1 in d:
                head = self.getContainingSet(d, n1)
                d[n2] = head
                d[head].add(n2)
            elif n2 in d:
                head = self.getContainingSet(d, n2)
                d[n1] = head
                d[head].add(n1)
                
            else:
                d[n1] = {n1, n2}
                d[n2] = n1
        
    def getContainingSet(self, d, n):
        if isinstance(d[n], set):
            return n
        else:
            return d[n]
            
            
            
            
#             x= {1,2}
#             d[1] = x
#             d[2] = x
            
#         {1:{1,2,3,4}, 2:{1}, 3:{1}, 4:{1}} 