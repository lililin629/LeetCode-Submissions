class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        d = {}  #{id:heap}
        
        for item in items:
            s_id = item[0]
            score = item[1]
            if s_id not in d:
                d[s_id] = []
                heapq.heapify(d[s_id] )
            heapq.heappush(d[s_id], score)
            if len(d[s_id]) > 5:
                heapq.heappop(d[s_id])
        
        result = []
        for student,scores in d.items():
            avg = sum(scores)//5
            result.append([student,avg])
        return result
            
            
                
            