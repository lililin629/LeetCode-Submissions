class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        d = {}  #{id:heap}
        
        for item in items:
            if item[0] not in d:
                d[item[0]] = []
                heapq.heapify(d[item[0]] )
            heapq.heappush(d[item[0]], item[1])
            if len(d[item[0]]) > 5:
                heapq.heappop(d[item[0]])
        
        result = []
        for student,scores in d.items():
            avg = sum(scores)//5
            result.append([student,avg])
        return result
            
            
                
            