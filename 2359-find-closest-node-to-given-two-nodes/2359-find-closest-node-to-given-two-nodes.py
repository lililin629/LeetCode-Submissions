class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # bfs(node1, node2)
        
        
        q1 = deque([node1])
        q2 = deque([node2])
        v1 = {}
        v2 = {}
        dis = 0
        ans = {}
       
        while q1 or q2:
            dis += 1
            if q1:
                cur1 = q1.popleft()
                v1[cur1] = dis
                if cur1 in v2:
                    max_dis = max(v1[cur1], v2[cur1])
                    if max_dis not in ans:
                        ans[max_dis] = [cur1]
                    else:
                        ans[max_dis].append(cur1)
                if edges[cur1] != -1 and edges[cur1] not in v1:
                    q1.append(edges[cur1])
            if q2:
                cur2 = q2.popleft()
                v2[cur2] = dis
                if cur2 in v1:
                    max_dis = max(v1[cur2], v2[cur2])
                    if max_dis not in ans:
                        ans[max_dis] = [cur2]
                    else:
                        ans[max_dis].append(cur2)
                if edges[cur2] != -1 and edges[cur2] not in v2:
                    q2.append(edges[cur2])
        if ans:
           
            ans = dict(sorted(ans.items()))
            
            for key in ans:
                ans[key].sort()
                return ans[key][0]
                break
                
        return -1
                
       

                    
        
        
        