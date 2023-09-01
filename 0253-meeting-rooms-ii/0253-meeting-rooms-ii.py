class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        # print(intervals)
        heap = [intervals[0][1]]
        heapq.heapify(heap)
        
        for interval in intervals[1:]:
            # print(heap)
            if heap:
                if heap[0] <= interval[0]:
                    heapq.heappop(heap)
                heapq.heappush(heap, interval[1])
        return len(heap)
            
                
            
        
                
                
        