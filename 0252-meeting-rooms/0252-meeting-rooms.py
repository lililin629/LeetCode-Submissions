class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort()
        heap = [intervals[0][1]]
        
        for interval in intervals[1:]:
            new_start = interval[0]
            if heap:
                cur_end = heap[0]
                if cur_end <= new_start:
                    heapq.heappop(heap)
                heapq.heappush(heap, interval[1])
        if len(heap) > 1:
            return False
        else:
            return True
                    
                    
            
        
        
        